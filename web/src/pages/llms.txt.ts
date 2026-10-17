import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { markdownResponse, siteSummary, sortByName } from '../utils/markdown';

// Index for LLMs and agents, following the https://llmstxt.org convention.
export const GET: APIRoute = async ({ site }) => {
  const loobins = sortByName(await getCollection('loobins'));
  const abs = (path: string) => new URL(path, site).href;

  const body = [
    '# LOOBins',
    '',
    `> ${siteSummary}`,
    '',
    'Each binary below links to a markdown version of its page. Entries list the binary paths, example ' +
      'commands (which are illustrative abuse examples, not detection signatures), the ATT&CK tactics ' +
      'they map to, and detection references. Built-in Unix binaries already covered by GTFOBins are ' +
      'only included when they have macOS-specific abuse.',
    '',
    '## Binaries',
    '',
    ...loobins.map((l) => `- [${l.data.name}](${abs(`/binaries/${l.id}.md`)}): ${l.data.short_description.trim()}`),
    '',
    '## Data',
    '',
    `- [loobins.json](${abs('/loobins.json')}): Every entry as structured JSON`,
    `- [llms-full.txt](${abs('/llms-full.txt')}): Every entry as a single markdown document`,
    '- [Schema](https://github.com/infosecB/LOOBins/blob/main/docs/schema.md): YAML schema for entries',
    '',
    '## Optional',
    '',
    '- [GitHub repository](https://github.com/infosecB/LOOBins): Source YAML and contribution guide',
    '- [PyLOOBins](https://pypi.org/project/pyloobins/): Python SDK and CLI with STIX 2 export',
    '',
  ].join('\n');

  return markdownResponse(body, 'text/plain');
};
