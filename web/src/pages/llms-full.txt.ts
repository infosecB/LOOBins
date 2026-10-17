import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { loobinMarkdown, markdownResponse, siteSummary, sortByName } from '../utils/markdown';

// The whole corpus as one markdown document, for loading into an LLM context in a single fetch.
export const GET: APIRoute = async ({ site }) => {
  const loobins = sortByName(await getCollection('loobins'));
  const header = `# LOOBins\n\n> ${siteSummary}\n\nSource: ${new URL('/', site).href}\n`;
  const entries = loobins.map((l) => loobinMarkdown(l, site!, 2));
  return markdownResponse([header, ...entries].join('\n---\n\n'), 'text/plain');
};
