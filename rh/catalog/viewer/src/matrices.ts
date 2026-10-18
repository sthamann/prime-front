import * as d3 from "d3";
import { heatColor } from "./palette";
import type { AppState } from "./state";
import type { MatrixBlock } from "./types";

export function renderMatrices(host: HTMLElement, state: AppState): () => void {
  host.innerHTML = "";
  host.className = "stage matrices-stage";
  const scroll = document.createElement("div");
  scroll.className = "matrix-scroll";
  host.append(scroll);

  const blocks: {
    title: string;
    data: MatrixBlock;
    rowKey: "family" | "kind";
    colKey: "outcome" | "failure_class";
  }[] = [
    {
      title: "family × outcome",
      data: state.bundle.matrix.family_x_outcome,
      rowKey: "family",
      colKey: "outcome",
    },
    {
      title: "family × failure class",
      data: state.bundle.matrix.family_x_failure_class,
      rowKey: "family",
      colKey: "failure_class",
    },
    {
      title: "kind × outcome",
      data: state.bundle.matrix.kind_x_outcome,
      rowKey: "kind",
      colKey: "outcome",
    },
  ];

  const cvd = state.bundle.matrix.curated_vs_draft;
  const banner = document.createElement("div");
  banner.className = "cvd";
  banner.innerHTML = `<span>curated <b>${cvd.curated}</b></span><span>draft <b>${cvd.draft}</b></span><span>needs review <b>${cvd.needs_review}</b></span>`;
  scroll.append(banner);

  const tooltip = document.createElement("div");
  tooltip.className = "tip";
  host.append(tooltip);

  for (const block of blocks) {
    const card = document.createElement("section");
    card.className = "matrix-card";
    const h = document.createElement("h2");
    h.textContent = block.title;
    card.append(h);
    const mount = document.createElement("div");
    mount.className = "svg-wrap matrix-wrap";
    card.append(mount);
    scroll.append(card);
    drawHeat(mount, block.data, block.rowKey, block.colKey, state, tooltip, host);
  }

  return () => {
    host.innerHTML = "";
  };
}

function drawHeat(
  mount: HTMLElement,
  block: MatrixBlock,
  rowKey: "family" | "kind",
  colKey: "outcome" | "failure_class",
  state: AppState,
  tooltip: HTMLElement,
  host: HTMLElement,
): void {
  const cellW = 36;
  const cellH = 18;
  const left = 200;
  const top = 88;
  const w = left + block.cols.length * cellW + 16;
  const h = top + block.rows.length * cellH + 12;
  const svg = d3
    .select(mount)
    .append("svg")
    .attr("class", "mx-svg")
    .attr("width", w)
    .attr("height", h)
    .attr("viewBox", `0 0 ${w} ${h}`);

  const max = d3.max(block.cells, (c) => c.n) || 1;
  const map = new Map(block.cells.map((c) => [`${c.row}\t${c.col}`, c.n]));

  svg
    .selectAll("text.col")
    .data(block.cols)
    .enter()
    .append("text")
    .attr("class", "col")
    .attr("transform", (_, i) => `translate(${left + i * cellW + cellW / 2},${top - 8}) rotate(-55)`)
    .attr("text-anchor", "start")
    .text((d) => d);

  svg
    .selectAll("text.row")
    .data(block.rows)
    .enter()
    .append("text")
    .attr("class", "row")
    .attr("x", left - 8)
    .attr("y", (_, i) => top + i * cellH + cellH * 0.72)
    .attr("text-anchor", "end")
    .text((d) => d.replace(/_/g, " "));

  const cells = svg
    .selectAll("rect.cell")
    .data(block.cells)
    .enter()
    .append("rect")
    .attr("class", "cell")
    .attr("x", (d) => left + block.cols.indexOf(d.col) * cellW + 1)
    .attr("y", (d) => top + block.rows.indexOf(d.row) * cellH + 1)
    .attr("width", cellW - 2)
    .attr("height", cellH - 2)
    .attr("rx", 2)
    .attr("fill", (d) => (d.n ? heatColor(Math.sqrt(d.n / max)) : "#161a22"))
    .attr("opacity", (d) => (d.n ? 1 : 0.4));

  cells
    .on("mouseenter", (ev, d) => {
      tooltip.hidden = false;
      tooltip.innerHTML = `<strong>${esc(d.row)}</strong><span>${esc(d.col)}</span><span>${d.n} records</span>`;
      const rect = host.getBoundingClientRect();
      tooltip.style.left = `${(ev as PointerEvent).clientX - rect.left + 12}px`;
      tooltip.style.top = `${(ev as PointerEvent).clientY - rect.top + 10}px`;
    })
    .on("mouseleave", () => {
      tooltip.hidden = true;
    })
    .on("click", (_, d) => {
      if (!d.n) return;
      state.applyMatrixCell(rowKey, d.row, colKey, d.col);
    });

  void map;
}

function esc(s: string): string {
  return s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);
}

export function matrixSvgEls(host: HTMLElement): SVGSVGElement[] {
  return [...host.querySelectorAll("svg.mx-svg")];
}
