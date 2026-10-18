import type { NextConfig } from "next";
const nextConfig: NextConfig = {
  reactStrictMode: true, poweredByHeader: false, compress: true,
  async redirects() { return [
    {source: "/:path*", has: [{type: "host", value: "prime-front-zeta.vercel.app"}], destination: "https://prime.fixpoint-theory.com/:path*", permanent: true},
    {source: "/prime-front", destination: "/research", permanent: true},
    {source: "/papers", destination: "/publications", permanent: true},
  ]; },
};
export default nextConfig;
