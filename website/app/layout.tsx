import type { Metadata, Viewport } from "next";
import { Inter, Newsreader, JetBrains_Mono } from "next/font/google";
import Link from "next/link";
import "./globals.css";
import "katex/dist/katex.min.css";
import { REPO_URL, SITE_URL } from "@/lib/utils";
const inter = Inter({ subsets: ["latin"], display: "swap", variable: "--font-inter" });
const serif = Newsreader({ subsets: ["latin"], display: "swap", variable: "--font-newsreader" });
const mono = JetBrains_Mono({ subsets: ["latin"], weight: ["400","500"], display: "swap", variable: "--font-jetbrains", preload: false });
const description = "Independent research on prime numbers, zeta operators and the Riemann Hypothesis. Read the research diary, papers, open questions and reproducible finite checks. No RH proof is claimed.";
export const viewport: Viewport = { themeColor: "#fcfbf8", colorScheme: "light", width: "device-width", initialScale: 1 };
export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL), title: {default: "Prime Front — primes, operators & open questions", template: "%s · Prime Front"},
  description, applicationName: "Prime Front", authors: [{name:"Stefan Hamann"},{name:"Alessandro Rizzo"}], category:"science",
  alternates: {canonical: SITE_URL},
  openGraph: {type:"website",siteName:"Prime Front",title:"Prime Front",description,url:SITE_URL,images:[{url:"/opengraph-image",width:1200,height:630,alt:"Prime Front · prime-number research"}]},
  twitter: {card:"summary_large_image",title:"Prime Front",description,images:["/opengraph-image"]},
  robots:{index:true,follow:true},
};
const nav = [["/research","Research diary"],["/publications","Publications"],["/verification","Verification"],["/method","Method"]];
export default function RootLayout({children}:{children:React.ReactNode}) { return (
 <html lang="en" className={`${inter.variable} ${serif.variable} ${mono.variable}`}><body>
 <a href="#main" className="sr-only focus:not-sr-only focus:fixed focus:top-2 focus:left-2 focus:z-50 bg-white p-3">Skip to main content</a>
 <header className="border-b border-slate-200 bg-[#fcfbf8]" ><div className="pf-wrap flex flex-wrap items-center justify-between gap-x-8 gap-y-4 py-5">
 <Link href="/" className="flex items-center gap-3 text-slate-950" aria-label="Prime Front home"><span className="flex size-10 items-center justify-center rounded-full border border-teal-800 font-serif text-2xl text-teal-900">p</span><span className="font-serif text-2xl font-semibold tracking-tight">Prime Front<span className="ml-1 text-teal-700">.</span></span></Link>
 <nav aria-label="Main navigation" className="pf-nav flex flex-wrap gap-x-6 gap-y-3 text-sm font-medium text-slate-600">{nav.map(([href,label])=><Link key={href} href={href}>{label}</Link>)}<a href={REPO_URL}>Source ↗</a></nav>
 </div></header>
 <main id="main">{children}</main>
 <footer className="pf-rule mt-12 py-10"><div className="pf-wrap flex flex-wrap justify-between gap-8 text-sm text-slate-600"><div><Link href="/" className="font-serif text-2xl text-slate-900">Prime Front.</Link><p className="mt-3 max-w-md leading-relaxed">Prime numbers, explicit formulas, and the limits of finite evidence.<br/>An independent open research project. No RH proof is claimed.</p></div><div className="space-y-3"><p>Stefan Hamann · Alessandro Rizzo</p><a className="pf-link block" href={REPO_URL}>Repository, source documents &amp; provenance ↗</a><p className="text-xs">Research originally developed alongside TFPT; published here independently.</p></div></div></footer>
 <script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify({"@context":"https://schema.org","@type":"ResearchProject",name:"Prime Front",url:SITE_URL,description,codeRepository:REPO_URL,sameAs:[REPO_URL]})}}/>
 </body></html>
 ); }
