# Prime Front website

Independent public home for the Prime Front research corpus. Next.js App Router, React and Tailwind CSS. The complete preserved research diary is at `/research`; `/prime-front` redirects there and incoming fragments survive. The video, captions, transcript and poster retain their original asset paths under `/prime-front/`.

## Local development

Use a supported Node.js version, run `npm ci`, then `npm run dev`. `npm run build` produces the production app. Deploy with `website/` as the project root. The canonical public origin is `https://prime-front.vercel.app` in `lib/utils.ts`.

## Source boundaries

- `components/primefront/`, `lib/primeFront.ts`, `lib/primeFrontArchive.ts`: preserved research narrative, diagrams, recent entries and lazy archive. Dated status labels and numerical counts are historical statements, not new claims.
- `lib/researchDocuments.ts`: preserved authored Hilbert–Pólya summary and dedicated contract sections extracted from the former shared publication index.
- `lib/verificationModules.json`: dedicated module inventory from the split ownership manifest. Source files under `public/verification/` are readable downloads; use the complete repository for execution and dependencies.
- `public/papers/`: dedicated RH/prime PDFs. Their source filenames are retained for traceability.

No RH proof is claimed. Finite checks, numerical measurements, conditional statements and open infinite/uniform problems remain distinct. Original source history is preserved in the repository provenance.
