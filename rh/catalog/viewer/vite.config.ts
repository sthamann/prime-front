import { defineConfig } from "vite";

export default defineConfig({
  root: ".",
  base: "./",
  publicDir: "public",
  build: {
    outDir: "dist",
    emptyOutDir: true,
    sourcemap: false,
  },
  server: { port: 5173, strictPort: false },
  preview: { port: 4173, strictPort: false },
});
