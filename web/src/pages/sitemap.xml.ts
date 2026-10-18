import type { APIRoute } from 'astro';

// @astrojs/sitemap only writes sitemap-index.xml and sitemap-N.xml. Crawlers and
// Search Console default to /sitemap.xml, so serve an index at that path too.
export const GET: APIRoute = ({ site }) => {
  const body =
    '<?xml version="1.0" encoding="UTF-8"?>' +
    '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
    `<sitemap><loc>${new URL('/sitemap-0.xml', site).href}</loc></sitemap>` +
    '</sitemapindex>';
  return new Response(body, { headers: { 'Content-Type': 'application/xml' } });
};
