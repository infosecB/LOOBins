import type { CollectionEntry } from 'astro:content';
import { formatDate, loobinTactics, tacticOrder } from './helpers';

type LOOBin = CollectionEntry<'loobins'>;

// Machine-readable markdown views of the corpus, served alongside the HTML
// pages for LLMs and agents (see /llms.txt).

export const siteSummary =
  'LOOBins (Living Off the Orchard: macOS Binaries) is a curated catalog of macOS built-in binaries ' +
  'that threat actors can abuse for post-exploitation, with example commands mapped to MITRE ATT&CK ' +
  'tactics, plus detection and reference links.';

// A fence one backtick longer than any run inside the code, so example commands can't break out.
function fence(code: string, lang = 'bash'): string {
  const longest = Math.max(0, ...(code.match(/`+/g) ?? []).map((run) => run.length));
  const ticks = '`'.repeat(Math.max(3, longest + 1));
  return `${ticks}${lang}\n${code.trim()}\n${ticks}`;
}

function link(name: string, href: string): string {
  return href.toLowerCase() === 'n/a' ? name : `[${name}](${href})`;
}

// `depth` sets the title's heading level so entries can nest inside a larger document.
export function loobinMarkdown(loobin: LOOBin, site: URL, depth = 1): string {
  const { data } = loobin;
  const h = (level: number) => '#'.repeat(depth + level - 1);
  const page = new URL(`/binaries/${loobin.id}/`, site).href;
  const lines: string[] = [
    `${h(1)} ${data.name}`,
    '',
    `> ${data.short_description}`,
    '',
    data.full_description.trim(),
    '',
    `- Page: ${page}`,
    `- Author: ${data.author}`,
    `- Created: ${formatDate(data.created)}`,
    `- Tactics: ${loobinTactics(loobin).join(', ') || 'None'}`,
    '',
    `${h(2)} Paths`,
    '',
    ...data.paths.map((p) => `- \`${p}\``),
    '',
    `${h(2)} Example Use Cases`,
  ];

  for (const uc of data.example_use_cases) {
    lines.push('', `${h(3)} ${uc.name}`, '', uc.description.trim(), '');
    if (uc.code) lines.push(fence(uc.code), '');
    const tactics = tacticOrder.filter((t) => uc.tactics.includes(t));
    if (tactics.length) lines.push(`- Tactics: ${tactics.join(', ')}`);
    if (uc.tags.length) lines.push(`- Tags: ${uc.tags.join(', ')}`);
  }

  lines.push('', `${h(2)} Detections`, '', ...data.detections.map((d) => `- ${link(d.name, d.url)}`));

  if (data.resources.length) {
    lines.push('', `${h(2)} Resources`, '', ...data.resources.map((r) => `- ${link(r.name, r.url)}`));
  }
  if (data.acknowledgements.length) {
    lines.push('', `${h(2)} Acknowledgements`, '', ...data.acknowledgements.map((a) => `- ${a}`));
  }

  return lines.join('\n').trimEnd() + '\n';
}

export function sortByName(loobins: LOOBin[]): LOOBin[] {
  return [...loobins].sort((a, b) => a.data.name.localeCompare(b.data.name));
}

export function markdownResponse(body: string, type = 'text/markdown'): Response {
  return new Response(body, { headers: { 'Content-Type': `${type}; charset=utf-8` } });
}
