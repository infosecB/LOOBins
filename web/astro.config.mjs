// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://infosecb.github.io',
  base: '/LOOBins',
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
