import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { formatDate } from '../utils/helpers';

// Generates a single downloadable JSON file containing every documented
// LOOBin. Served as a static file at /loobins.json at build time.
export const GET: APIRoute = async () => {
  const loobins = await getCollection('loobins');

  const data = loobins
    .sort((a, b) => a.data.name.localeCompare(b.data.name))
    .map((loobin) => ({
      ...loobin.data,
      created: formatDate(loobin.data.created),
    }));

  return new Response(JSON.stringify(data, null, 2), {
    headers: {
      'Content-Type': 'application/json',
      'Content-Disposition': 'attachment; filename="loobins.json"',
    },
  });
};
