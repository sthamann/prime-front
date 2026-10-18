/** Pure export formatters — usable from the browser and from Node. */

export interface ExportNode {
  id: string;
  path: string;
  round: string;
  kind: string;
  family: string;
  outcome: string;
  failure_class: string;
  rh_relevance: string;
  draft: boolean;
  score: number;
  question?: string;
  mechanism?: string;
}

export interface ExportEdge {
  source: string;
  target: string;
  type: string;
  weight?: number;
}

function xmlEscape(s: string): string {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

function csvEscape(s: unknown): string {
  const t = s == null ? "" : String(s);
  if (/[",\n]/.test(t)) return `"${t.replace(/"/g, '""')}"`;
  return t;
}

export function recordsCsv(nodes: ExportNode[]): string {
  const cols = [
    "id",
    "path",
    "round",
    "kind",
    "family",
    "outcome",
    "failure_class",
    "rh_relevance",
    "draft",
    "score",
    "question",
    "mechanism",
  ] as const;
  const lines = [cols.join(",")];
  for (const n of nodes) {
    lines.push(
      cols
        .map((c) => csvEscape(n[c]))
        .join(","),
    );
  }
  return lines.join("\n") + "\n";
}

export function matrixCsv(block: {
  rows: string[];
  cols: string[];
  cells: { row: string; col: string; n: number }[];
}): string {
  const map = new Map<string, number>();
  for (const c of block.cells) map.set(`${c.row}\t${c.col}`, c.n);
  const lines = ["row," + block.cols.map(csvEscape).join(",")];
  for (const r of block.rows) {
    const vals = block.cols.map((c) => String(map.get(`${r}\t${c}`) ?? 0));
    lines.push([csvEscape(r), ...vals].join(","));
  }
  return lines.join("\n") + "\n";
}

export function toGraphML(nodes: ExportNode[], edges: ExportEdge[]): string {
  const nodeXml = nodes
    .map(
      (n) =>
        `    <node id="${xmlEscape(n.id)}">
      <data key="path">${xmlEscape(n.path)}</data>
      <data key="round">${xmlEscape(n.round)}</data>
      <data key="family">${xmlEscape(n.family)}</data>
      <data key="outcome">${xmlEscape(n.outcome)}</data>
      <data key="kind">${xmlEscape(n.kind)}</data>
      <data key="score">${n.score}</data>
      <data key="draft">${n.draft}</data>
    </node>`,
    )
    .join("\n");
  const edgeXml = edges
    .map(
      (e, i) =>
        `    <edge id="e${i}" source="${xmlEscape(e.source)}" target="${xmlEscape(e.target)}">
      <data key="etype">${xmlEscape(e.type)}</data>
    </edge>`,
    )
    .join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <key id="path" for="node" attr.name="path" attr.type="string"/>
  <key id="round" for="node" attr.name="round" attr.type="string"/>
  <key id="family" for="node" attr.name="family" attr.type="string"/>
  <key id="outcome" for="node" attr.name="outcome" attr.type="string"/>
  <key id="kind" for="node" attr.name="kind" attr.type="string"/>
  <key id="score" for="node" attr.name="score" attr.type="double"/>
  <key id="draft" for="node" attr.name="draft" attr.type="boolean"/>
  <key id="etype" for="edge" attr.name="type" attr.type="string"/>
  <graph id="G" edgedefault="undirected">
${nodeXml}
${edgeXml}
  </graph>
</graphml>
`;
}

export function toGEXF(nodes: ExportNode[], edges: ExportEdge[]): string {
  const now = new Date().toISOString();
  const nodeXml = nodes
    .map(
      (n) =>
        `      <node id="${xmlEscape(n.id)}" label="${xmlEscape(n.round || n.path)}">
        <attvalues>
          <attvalue for="family" value="${xmlEscape(n.family)}"/>
          <attvalue for="outcome" value="${xmlEscape(n.outcome)}"/>
          <attvalue for="kind" value="${xmlEscape(n.kind)}"/>
          <attvalue for="score" value="${n.score}"/>
        </attvalues>
      </node>`,
    )
    .join("\n");
  const edgeXml = edges
    .map(
      (e, i) =>
        `      <edge id="e${i}" source="${xmlEscape(e.source)}" target="${xmlEscape(e.target)}" weight="${e.weight ?? 1}">
        <attvalues><attvalue for="etype" value="${xmlEscape(e.type)}"/></attvalues>
      </edge>`,
    )
    .join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>
<gexf xmlns="http://gexf.net/1.3" version="1.3">
  <meta lastmodifieddate="${now}">
    <creator>rh-catalog-viewer</creator>
    <description>RH corpus catalog — exploration record; no RH claim</description>
  </meta>
  <graph defaultedgetype="undirected">
    <attributes class="node">
      <attribute id="family" title="family" type="string"/>
      <attribute id="outcome" title="outcome" type="string"/>
      <attribute id="kind" title="kind" type="string"/>
      <attribute id="score" title="score" type="float"/>
    </attributes>
    <attributes class="edge">
      <attribute id="etype" title="type" type="string"/>
    </attributes>
    <nodes>
${nodeXml}
    </nodes>
    <edges>
${edgeXml}
    </edges>
  </graph>
</gexf>
`;
}

export function simpleNetworkSvg(
  nodes: { id: string; family: string; x: number; y: number; r: number }[],
  edges: { x1: number; y1: number; x2: number; y2: number; type: string }[],
  w: number,
  h: number,
  colors: Record<string, string>,
): string {
  const lines = edges
    .map(
      (e) =>
        `<line x1="${e.x1.toFixed(1)}" y1="${e.y1.toFixed(1)}" x2="${e.x2.toFixed(1)}" y2="${e.y2.toFixed(1)}" stroke="#5a6270" stroke-width="0.6" opacity="0.35"/>`,
    )
    .join("");
  const circles = nodes
    .map((n) => {
      const fill = colors[n.family] || "#8b919d";
      return `<circle cx="${n.x.toFixed(1)}" cy="${n.y.toFixed(1)}" r="${n.r}" fill="${fill}" stroke="#0b0d12" stroke-width="0.6"/>`;
    })
    .join("");
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">
  <rect width="${w}" height="${h}" fill="#0b0d12"/>
  <g>${lines}</g>
  <g>${circles}</g>
</svg>
`;
}

export function serializeSvgElement(svg: SVGSVGElement): string {
  const clone = svg.cloneNode(true) as SVGSVGElement;
  clone.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  const walk = (src: Element, dst: Element) => {
    const cs = getComputedStyle(src);
    const keep = [
      "fill",
      "stroke",
      "stroke-width",
      "stroke-dasharray",
      "opacity",
      "font-family",
      "font-size",
      "font-weight",
      "text-anchor",
      "paint-order",
    ];
    const parts: string[] = [];
    for (const k of keep) {
      const v = cs.getPropertyValue(k);
      if (v) parts.push(`${k}:${v}`);
    }
    if (parts.length) dst.setAttribute("style", parts.join(";"));
    const sa = src.children;
    const da = dst.children;
    for (let i = 0; i < sa.length; i++) walk(sa[i], da[i]);
  };
  walk(svg, clone);
  return `<?xml version="1.0" encoding="UTF-8"?>\n` + new XMLSerializer().serializeToString(clone);
}

export interface ConceptExportNode {
  id: string;
  name: string;
  type: string;
  status: string;
  alive: boolean;
  attempt_count: number;
}

export interface ConceptExportEdge {
  src: string;
  dst: string;
  rel: string;
  strength: string;
  note?: string;
}

export function conceptsCsv(nodes: ConceptExportNode[], edges: ConceptExportEdge[]): { nodes: string; edges: string } {
  const nCols = ["id", "name", "type", "status", "alive", "attempt_count"] as const;
  const eCols = ["src", "dst", "rel", "strength", "note"] as const;
  const nLines = [nCols.join(",")];
  for (const n of nodes) nLines.push(nCols.map((c) => csvEscape(n[c])).join(","));
  const eLines = [eCols.join(",")];
  for (const e of edges) eLines.push(eCols.map((c) => csvEscape(e[c])).join(","));
  return { nodes: nLines.join("\n") + "\n", edges: eLines.join("\n") + "\n" };
}

export function conceptsGraphML(nodes: ConceptExportNode[], edges: ConceptExportEdge[]): string {
  const nodeXml = nodes
    .map(
      (n) =>
        `    <node id="${xmlEscape(n.id)}">
      <data key="name">${xmlEscape(n.name)}</data>
      <data key="type">${xmlEscape(n.type)}</data>
      <data key="status">${xmlEscape(n.status)}</data>
      <data key="alive">${n.alive}</data>
      <data key="attempts">${n.attempt_count}</data>
    </node>`,
    )
    .join("\n");
  const edgeXml = edges
    .map(
      (e, i) =>
        `    <edge id="e${i}" source="${xmlEscape(e.src)}" target="${xmlEscape(e.dst)}">
      <data key="rel">${xmlEscape(e.rel)}</data>
      <data key="strength">${xmlEscape(e.strength)}</data>
    </edge>`,
    )
    .join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <key id="name" for="node" attr.name="name" attr.type="string"/>
  <key id="type" for="node" attr.name="type" attr.type="string"/>
  <key id="status" for="node" attr.name="status" attr.type="string"/>
  <key id="alive" for="node" attr.name="alive" attr.type="boolean"/>
  <key id="attempts" for="node" attr.name="attempt_count" attr.type="int"/>
  <key id="rel" for="edge" attr.name="rel" attr.type="string"/>
  <key id="strength" for="edge" attr.name="strength" attr.type="string"/>
  <graph id="concepts" edgedefault="directed">
${nodeXml}
${edgeXml}
  </graph>
</graphml>
`;
}

export function conceptsGEXF(nodes: ConceptExportNode[], edges: ConceptExportEdge[]): string {
  const now = new Date().toISOString();
  const nodeXml = nodes
    .map(
      (n) =>
        `      <node id="${xmlEscape(n.id)}" label="${xmlEscape(n.name)}">
        <attvalues>
          <attvalue for="type" value="${xmlEscape(n.type)}"/>
          <attvalue for="status" value="${xmlEscape(n.status)}"/>
          <attvalue for="alive" value="${n.alive}"/>
        </attvalues>
      </node>`,
    )
    .join("\n");
  const edgeXml = edges
    .map(
      (e, i) =>
        `      <edge id="e${i}" source="${xmlEscape(e.src)}" target="${xmlEscape(e.dst)}">
        <attvalues><attvalue for="rel" value="${xmlEscape(e.rel)}"/></attvalues>
      </edge>`,
    )
    .join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>
<gexf xmlns="http://gexf.net/1.3" version="1.3">
  <meta lastmodifieddate="${now}">
    <creator>rh-catalog-viewer</creator>
    <description>RH corpus catalog — exploration record; no RH claim</description>
  </meta>
  <graph defaultedgetype="directed">
    <attributes class="node">
      <attribute id="type" title="type" type="string"/>
      <attribute id="status" title="status" type="string"/>
      <attribute id="alive" title="alive" type="boolean"/>
    </attributes>
    <attributes class="edge">
      <attribute id="rel" title="rel" type="string"/>
    </attributes>
    <nodes>
${nodeXml}
    </nodes>
    <edges>
${edgeXml}
    </edges>
  </graph>
</gexf>
`;
}

export function conceptsDot(nodes: ConceptExportNode[], edges: ConceptExportEdge[]): string {
  const n = nodes
    .map((x) => `  "${x.id}" [label="${xmlEscape(x.name).replace(/"/g, '\\"')}\\n${x.type}"];`)
    .join("\n");
  const e = edges.map((x) => `  "${x.src}" -> "${x.dst}" [label="${x.rel}"];`).join("\n");
  return `digraph concepts {\n  graph [label="RH corpus catalog — exploration record; no RH claim"];\n${n}\n${e}\n}\n`;
}

export function edgeEndpoints(
  edges: { source: string | { id: string }; target: string | { id: string }; type: string }[],
): ExportEdge[] {
  return edges.map((e) => ({
    source: typeof e.source === "string" ? e.source : e.source.id,
    target: typeof e.target === "string" ? e.target : e.target.id,
    type: e.type,
  }));
}
