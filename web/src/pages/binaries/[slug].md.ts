import type { APIRoute, GetStaticPaths } from 'astro';
import { getCollection } from 'astro:content';
import { loobinMarkdown, markdownResponse } from '../../utils/markdown';

// Markdown twin of each binary page, e.g. /binaries/osascript.md.
export const getStaticPaths: GetStaticPaths = async () => {
  const loobins = await getCollection('loobins');
  return loobins.map((loobin) => ({ params: { slug: loobin.id }, props: { loobin } }));
};

export const GET: APIRoute = ({ props, site }) => markdownResponse(loobinMarkdown(props.loobin, site!));
