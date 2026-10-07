// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://loobins.io',
  base: '/',
  integrations: [
    sitemap({
      // /tactics/ and /tags/ only hold redirect stubs now.
      filter: (page) => !/\/(tactics|tags)\//.test(new URL(page).pathname),
    }),
  ],
  redirects: {
    // The tactic and tag index pages were folded into the /binaries/ filters.
    '/tactics': '/binaries/',
    '/tags': '/binaries/',
    // Used By is now a section of the About page.
    '/used-by': '/about/#used-by',
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
