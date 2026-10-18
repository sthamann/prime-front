import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";
export function cn(...inputs: ClassValue[]) { return twMerge(clsx(inputs)); }
export const REPO_URL = "https://github.com/sthamann/prime-front";
export const SITE_URL = "https://prime-front-zeta.vercel.app";
