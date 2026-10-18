import * as d3 from "d3";
import { familyColor, outcomeStroke } from "./palette";
import type { AppState } from "./state";
import type { TimelineItem } from "./types";

export function renderTimeline(host: HTMLElement, state: AppState): () => void {
  host.innerHTML = "";
  host.className = "stage timeline-stage";
  const wrap = document.createElement("div");
  wrap.className = "svg-wrap";
  const tooltip = document.createElement("div");
  tooltip.className = "tip";
  host.append(wrap, tooltip);

  const svg = d3.select(wrap).append("svg").attr("class", "tl-svg").attr("aria-label", "Round timeline");
  const g = svg.append("g");

  function draw(): void {
    const data = state.bundle.timeline;
    const families = state.bundle.graph.meta.orders.families.filter((f) =>
      state.filters.families.has(f),
    );
    const items = data.items.filter((it) => {
      if (it.round_num < 0) return false;
      if (!state.filters.families.has(it.family)) return false;
      if (!state.filters.outcomes.has(it.outcome)) return false;
      if (state.filters.curatedOnly && it.draft) return false;
      return true;
    });

    const w = wrap.clientWidth || 800;
    const laneH = 22;
    const top = 36;
    const bottom = 48;
    const left = 168;
    const h = Math.max(320, top + families.length * laneH + bottom);
    svg.attr("viewBox", `0 0 ${w} ${h}`).attr("width", w).attr("height", h);

    const x = d3
      .scaleLinear()
      .domain([data.min_round, data.max_round || 1])
      .range([left, w - 24]);
    const y = d3
      .scaleBand<string>()
      .domain(families)
      .range([top, top + families.length * laneH])
      .padding(0.18);

    g.selectAll("*").remove();

    g.append("g")
      .attr("class", "axis")
      .attr("transform", `translate(0,${top - 8})`)
      .call(d3.axisTop(x).ticks(10).tickFormat((d) => `r${d}`));

    g.selectAll("rect.lane")
      .data(families)
      .enter()
      .append("rect")
      .attr("class", "lane")
      .attr("x", left)
      .attr("y", (d) => y(d) ?? 0)
      .attr("width", w - left - 24)
      .attr("height", y.bandwidth())
      .attr("fill", (d) => familyColor(d))
      .attr("opacity", 0.06);

    g.selectAll("text.lane-lab")
      .data(families)
      .enter()
      .append("text")
      .attr("class", "lane-lab")
      .attr("x", left - 8)
      .attr("y", (d) => (y(d) ?? 0) + y.bandwidth() / 2 + 4)
      .attr("text-anchor", "end")
      .text((d) => d.replace(/_/g, " ").slice(0, 22));

    const jitter = (id: string) => ((hash(id) % 100) / 100 - 0.5) * y.bandwidth() * 0.45;

    const dots = g
      .selectAll("circle.glyph")
      .data(items, (d) => (d as TimelineItem).id)
      .enter()
      .append("circle")
      .attr("class", "glyph")
      .attr("cx", (d) => x(d.round_num))
      .attr("cy", (d) => (y(d.family) ?? 0) + y.bandwidth() / 2 + jitter(d.id))
      .attr("r", (d) => 2.4 + Math.sqrt(d.score))
      .attr("fill", (d) => familyColor(d.family))
      .attr("stroke", (d) => outcomeStroke(d.outcome))
      .attr("stroke-width", 1.1)
      .attr("opacity", (d) => (d.draft ? 0.45 : 0.92));

    dots
      .on("mouseenter", (ev, d) => {
        tooltip.hidden = false;
        tooltip.innerHTML = `<strong>${esc(d.round)}</strong><span>${esc(d.family)}</span><span>${esc(d.outcome)}</span>`;
        const rect = host.getBoundingClientRect();
        tooltip.style.left = `${(ev as PointerEvent).clientX - rect.left + 12}px`;
        tooltip.style.top = `${(ev as PointerEvent).clientY - rect.top + 10}px`;
      })
      .on("mouseleave", () => {
        tooltip.hidden = true;
      })
      .on("click", (ev, d) => {
        ev.stopPropagation();
        const node = state.bundle.graph.nodes.find((n) => n.id === d.id) || null;
        state.select(node);
      });

    const brush = d3
      .brushX()
      .extent([
        [left, top - 4],
        [w - 24, top + families.length * laneH + 4],
      ])
      .on("end", (ev) => {
        if (!ev.selection) return;
        const [a, b] = ev.selection as [number, number];
        const r0 = Math.round(x.invert(a));
        const r1 = Math.round(x.invert(b));
        state.applyRoundBrush(Math.min(r0, r1), Math.max(r0, r1));
      });
    g.append("g").attr("class", "brush").call(brush);
  }

  const off = state.on(() => {
    if (state.view === "timeline") draw();
  });
  const ro = new ResizeObserver(() => draw());
  ro.observe(wrap);
  draw();
  return () => {
    off();
    ro.disconnect();
    host.innerHTML = "";
  };
}

function hash(s: string): number {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 16777619);
  return h >>> 0;
}

function esc(s: string): string {
  return s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);
}
