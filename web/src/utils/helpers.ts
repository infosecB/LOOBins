const base = import.meta.env.BASE_URL.replace(/\/$/, '');

export function url(path: string): string {
  return `${base}${path}`;
}

// Link into the /binaries/ filter UI. Tactics are matched by slug, tags by exact value.
export function filterUrl(facet: 'tactic' | 'tag', value: string): string {
  const param = facet === 'tactic' ? slugify(value) : value;
  return url(`/binaries/?${new URLSearchParams({ [facet]: param })}`);
}

export function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
}

export function loobinTags(loobin: any): string[] {
  return [...new Set<string>(loobin.data.example_use_cases.flatMap((uc: any) => uc.tags ?? []))];
}

// Relative to build time; the site redeploys whenever a LOOBin is added.
const NEW_WINDOW_MS = 90 * 24 * 60 * 60 * 1000;

export function isNew(created: Date): boolean {
  return Date.now() - created.getTime() < NEW_WINDOW_MS;
}

export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}

// Tactic colors only fill a small dot beside neutral text, so lighter shades read better on the dark surface.
const tacticColors: Record<string, string> = {
  'Reconnaissance': 'bg-blue-400',
  'Resource Development': 'bg-indigo-400',
  'Initial Access': 'bg-violet-400',
  'Execution': 'bg-red-400',
  'Persistence': 'bg-orange-400',
  'Privilege Escalation': 'bg-amber-400',
  'Stealth': 'bg-yellow-400',
  'Defense Impairment': 'bg-stone-400',
  'Credential Access': 'bg-lime-400',
  'Discovery': 'bg-green-400',
  'Lateral Movement': 'bg-emerald-400',
  'Collection': 'bg-teal-400',
  'Exfiltration': 'bg-cyan-400',
  'Command and Control': 'bg-sky-400',
  'Impact': 'bg-rose-400',
};

// Tactics in ATT&CK kill-chain order.
export const tacticOrder = Object.keys(tacticColors);

export function loobinTactics(loobin: any): string[] {
  const tactics = new Set<string>(loobin.data.example_use_cases.flatMap((uc: any) => uc.tactics ?? []));
  return tacticOrder.filter((t) => tactics.has(t));
}

export function tacticColor(tactic: string): string {
  return tacticColors[tactic] ?? 'bg-slate-400';
}
