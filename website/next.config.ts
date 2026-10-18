import type { NextConfig } from "next";
const nextConfig: NextConfig = {
  reactStrictMode: true, poweredByHeader: false, compress: true,
  async redirects() { return [
    {source: "/prime-front", destination: "/research", permanent: true},
    {source: "/papers", destination: "/publications", permanent: true},
  ]; },
};
export default nextConfig;
