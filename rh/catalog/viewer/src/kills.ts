import * as d3 from "d3";
import { heatColor } from "./palette";
import type { AppState } from "./state";
import type { KillCluster, MissItem } from "./types";

export function renderKills(host: HTMLElement, state: AppState): () => void {
  host.innerHTML = "";
  host.className = "stage kills-stage";
  const scroll = document.createElement("div");
  scroll.className = "kills-scroll";
  host.append(scroll);

  const kills = state.bundle.kills;
  const sun = document.createElement("section");
  sun.className = "kill-card";
  sun.innerHTML = `<h2>Kill roots</h2><p class="muted">${kills.killed_total ?? "—"} killed records in the paths report (curated slice).</p>`;
  const sunMount = document.createElement("div");
  sunMount.className = "svg-wrap sun-wrap";
  const members = document.createElement("div");
  members.className = "member-list";
  members.innerHTML = `<p class="muted">Click a slice.</p>`;
  sun.append(sunMount, members);
  scroll.append(sun);

  drawSunburst(sunMount, kills.clusters, (c) => {
    members.innerHTML = `<h3>${esc(c.root_phrase || c.failure_class || "cluster")}</h3>
      <p class="muted">${c.count} · ${esc(c.structural_root || "")}</p>
      <ul>${(c.members || [])
        .map(
          (m) =>
            `<li><a href="${fileHref(m.path)}" data-path="${esc(m.path)}">${esc(m.round)}</a> <code>${esc(m.path)}</code></li>`,
        )
        .join("")}</ul>`;
    members.querySelectorAll("a[data-path]").forEach((a) => {
      a.addEventListener("click", (ev) => {
        ev.preventDefault();
        const path = (a as HTMLElement).dataset.path || "";
        const node = state.bundle.graph.nodes.find((n) => n.path === path) || null;
        if (node) {
          state.select(node);
          state.setView("network");
        }
      });
    });
  });

  scroll.append(
    tableSection(
      "Orphans",
      ["rank", "round", "family", "path", "potential"],
      state.bundle.orphans.ranked.map((r) => ({
        rank: String(r.rank),
        round: r.round,
        family: r.family,
        path: r.path,
        potential: r.potential,
      })),
      state,
    ),
    tableSection(
      "Untried pairs",
      ["a", "b", "screen", "constraint", "why"],
      state.bundle.pairs.pairs.map((p) => ({
        a: p.a,
        b: p.b,
        screen: p.screen,
        constraint: p.constraint,
        why: p.why,
      })),
      state,
    ),
    tableSection(
      "Conflicts",
      ["object", "family", "n", "reconciliation"],
      state.bundle.conflicts.items.map((c) => ({
        object: c.object,
        family: c.family,
        n: String((c.records || []).length),
        reconciliation: c.reconciliation,
      })),
      state,
    ),
    missesSection(state.bundle.misses.nearest_misses, state.bundle.misses.verdict, state),
  );

  return () => {
    host.innerHTML = "";
  };
}

function drawSunburst(
  mount: HTMLElement,
  clusters: KillCluster[],
  onPick: (c: KillCluster) => void,
): void {
  const size = 420;
  const svg = d3
    .select(mount)
    .append("svg")
    .attr("class", "sun-svg")
    .attr("width", size)
    .attr("height", size)
    .attr("viewBox", `0 0 ${size} ${size}`);
  if (!clusters.length) {
    svg.append("text").attr("x", size / 2).attr("y", size / 2).attr("text-anchor", "middle").attr("class", "muted").text("No clusters");
    return;
  }
  const root = d3
    .hierarchy({
      name: "kills",
      children: clusters.map((c) => ({
        name: c.root_phrase || c.failure_class || "?",
        value: c.count,
        cluster: c,
      })),
    } as d3.HierarchyNode<unknown>["data"] & { children?: unknown[]; value?: number })
    .sum((d) => (d as { value?: number }).value || 0)
    .sort((a, b) => (b.value || 0) - (a.value || 0));

  const partition = d3.partition<typeof root.data>().size([2 * Math.PI, size / 2 - 12]);
  const arc = d3
    .arc<d3.HierarchyRectangularNode<typeof root.data>>()
    .startAngle((d) => d.x0)
    .endAngle((d) => d.x1)
    .innerRadius((d) => d.y0)
    .outerRadius((d) => d.y1 - 1);

  const g = svg.append("g").attr("transform", `translate(${size / 2},${size / 2})`);
  const max = root.value || 1;
  const nodes = partition(root).descendants().filter((d) => d.depth === 1);
  g.selectAll("path")
    .data(nodes)
    .enter()
    .append("path")
    .attr("d", (d) => arc(d as d3.HierarchyRectangularNode<typeof root.data>) || "")
    .attr("fill", (d) => heatColor(Math.sqrt((d.value || 0) / max)))
    .attr("stroke", "#0b0d12")
    .attr("stroke-width", 1)
    .style("cursor", "pointer")
    .on("click", (_, d) => {
      const c = (d.data as { cluster?: KillCluster }).cluster;
      if (c) onPick(c);
    });

  g.selectAll("text")
    .data(nodes.filter((d) => d.x1 - d.x0 > 0.18))
    .enter()
    .append("text")
    .attr("class", "sun-lab")
    .attr("transform", (d) => {
      const a = (((d.x0 + d.x1) / 2) * 180) / Math.PI - 90;
      const r = (d.y0 + d.y1) / 2;
      return `rotate(${a}) translate(${r},0) rotate(${a < 90 && a > -90 ? 0 : 180})`;
    })
    .attr("dy", "0.35em")
    .attr("text-anchor", "middle")
    .text((d) => String((d.data as { name?: string }).name || "").slice(0, 22));
}

function tableSection(
  title: string,
  cols: string[],
  rows: Record<string, string>[],
  state: AppState,
): HTMLElement {
  const sec = document.createElement("section");
  sec.className = "kill-card";
  const head = document.createElement("div");
  head.className = "table-head";
  head.innerHTML = `<h2>${esc(title)}</h2><span class="muted">${rows.length}</span>`;
  const table = document.createElement("table");
  table.className = "data-table";
  const thead = document.createElement("thead");
  thead.innerHTML = `<tr>${cols.map((c) => `<th data-col="${esc(c)}">${esc(c)}</th>`).join("")}</tr>`;
  const tbody = document.createElement("tbody");
  let sortCol = cols[0];
  let asc = true;

  const paint = () => {
    const sorted = rows.slice().sort((a, b) => {
      const va = a[sortCol] || "";
      const vb = b[sortCol] || "";
      const na = Number(va);
      const nb = Number(vb);
      if (!Number.isNaN(na) && !Number.isNaN(nb) && va !== "" && vb !== "") {
        return asc ? na - nb : nb - na;
      }
      return asc ? va.localeCompare(vb) : vb.localeCompare(va);
    });
    tbody.innerHTML = sorted
      .map((r) => {
        const cells = cols
          .map((c) => {
            const v = r[c] || "";
            if (c === "path") {
              return `<td><a href="${fileHref(v)}" data-path="${esc(v)}">${esc(v)}</a></td>`;
            }
            if (c === "screen") {
              return `<td><span class="tag tag-${esc(v.toLowerCase())}">${esc(v)}</span></td>`;
            }
            return `<td>${esc(v)}</td>`;
          })
          .join("");
        return `<tr>${cells}</tr>`;
      })
      .join("");
    tbody.querySelectorAll("a[data-path]").forEach((a) => {
      a.addEventListener("click", (ev) => {
        ev.preventDefault();
        const path = (a as HTMLElement).dataset.path || "";
        const node = state.bundle.graph.nodes.find((n) => n.path === path) || null;
        if (node) {
          state.select(node);
          state.setView("network");
        }
      });
    });
  };

  thead.querySelectorAll("th").forEach((th) => {
    th.addEventListener("click", () => {
      const c = (th as HTMLElement).dataset.col || cols[0];
      if (c === sortCol) asc = !asc;
      else {
        sortCol = c;
        asc = true;
      }
      paint();
    });
  });
  table.append(thead, tbody);
  sec.append(head, table);
  paint();
  return sec;
}

function missesSection(items: MissItem[], verdict: string, state: AppState): HTMLElement {
  const sec = document.createElement("section");
  sec.className = "kill-card";
  sec.innerHTML = `<h2>Nearest misses</h2><p class="muted">${esc(verdict)}</p>`;
  const table = document.createElement("table");
  table.className = "data-table";
  table.innerHTML = `<thead><tr><th>name</th><th>assessment</th><th>chain</th></tr></thead><tbody>${items
    .map((m) => {
      const chain = (m.chain || [])
        .map(
          (c) =>
            `<a href="${fileHref(c.path)}" data-path="${esc(c.path)}">${esc(c.round)}</a>`,
        )
        .join(" → ");
      return `<tr><td>${esc(m.name)}</td><td>${esc(m.assessment || "")}</td><td>${chain}</td></tr>`;
    })
    .join("")}</tbody>`;
  table.querySelectorAll("a[data-path]").forEach((a) => {
    a.addEventListener("click", (ev) => {
      ev.preventDefault();
      const path = (a as HTMLElement).dataset.path || "";
      const node = state.bundle.graph.nodes.find((n) => n.path === path) || null;
      if (node) {
        state.select(node);
        state.setView("network");
      }
    });
  });
  sec.append(table);
  return sec;
}

function fileHref(rel: string): string {
  return `cursor://file/${rel}`;
}

function esc(s: string): string {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);
}
