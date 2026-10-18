#!/usr/bin/env node
/** Copy gaps_report.json into public/data. concepts.json is written by build_map.py. */
import { copyFile, mkdir } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const viewer = join(dirname(fileURLToPath(import.meta.url)), "..");
const src = join(viewer, "..", "map", "gaps_report.json");
const destDir = join(viewer, "public", "data");
const dest = join(destDir, "gaps_report.json");
await mkdir(destDir, { recursive: true });
try {
  await copyFile(src, dest);
  console.log("copied", dest);
} catch (err) {
  console.warn("gaps_report.json not copied:", err instanceof Error ? err.message : err);
}
