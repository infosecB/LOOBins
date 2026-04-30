// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://infosecb.github.io',
  base: '/LOOBins',
  integrations: [],
  vite: {
    plugins: [tailwindcss()],
  },
});
