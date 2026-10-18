import type { MetadataRoute } from "next";
import { SITE_URL } from "@/lib/utils";
import extractedPublications from "@/lib/extractedPublications.json";
import { publications } from "@/lib/publications";
export default function sitemap():MetadataRoute.Sitemap{return ["","/research","/publications","/verification","/method",...publications.map(p=>`/papers/${p.slug}`),...publications.map(p=>`/papers/${p.file}.pdf`),...extractedPublications.map(p=>`/papers/${p.file}.pdf`)].map(path=>({url:`${SITE_URL}${path}`,lastModified:"2026-10-18",changeFrequency:"monthly" as const,priority:path===""?1:path.endsWith(".pdf")?.5:.8}))}
