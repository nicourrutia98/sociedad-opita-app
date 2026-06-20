// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';

// Sociedad Opita — Astro 5 + Cloudflare Pages + React islands + Tailwind
// BE: AWS Lambda (FastAPI + Mangum) — no vive en este repo, expuesto vía API Gateway
// Data: cities/tello/*.yaml + perfiles_psicometricos.py (Python, fuera de scope FE)
export default defineConfig({
  site: 'https://sociedad.opitacode.com',
  output: 'static',
  adapter: cloudflare({
    platformProxy: { enabled: true },
  }),
  integrations: [
    react({ include: ['**/components/**/*.{tsx,jsx}'] }),
    tailwind({ applyBaseStyles: true }),
    mdx(),
  ],
  vite: {
    ssr: {
      noExternal: ['d3', 'pixi.js'],
    },
  },
  build: {
    inlineStylesheets: 'auto',
  },
  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'viewport',
  },
});
