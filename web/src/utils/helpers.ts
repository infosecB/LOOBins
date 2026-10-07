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

// Shades are chosen so white badge text meets WCAG AA (>= 4.5:1).
const tacticColors: Record<string, string> = {
  'Reconnaissance': 'bg-blue-600',
  'Resource Development': 'bg-indigo-600',
  'Initial Access': 'bg-violet-600',
  'Execution': 'bg-red-600',
  'Persistence': 'bg-orange-700',
  'Privilege Escalation': 'bg-amber-700',
  'Defense Evasion': 'bg-yellow-700',
  'Credential Access': 'bg-lime-700',
  'Discovery': 'bg-green-700',
  'Lateral Movement': 'bg-emerald-700',
  'Collection': 'bg-teal-700',
  'Exfiltration': 'bg-cyan-700',
  'Command and Control': 'bg-sky-700',
  'Impact': 'bg-rose-600',
};

// Tactics in ATT&CK kill-chain order.
export const tacticOrder = Object.keys(tacticColors);

export function loobinTactics(loobin: any): string[] {
  const tactics = new Set<string>(loobin.data.example_use_cases.flatMap((uc: any) => uc.tactics ?? []));
  return tacticOrder.filter((t) => tactics.has(t));
}

export function tacticColor(tactic: string): string {
  return tacticColors[tactic] ?? 'bg-slate-600';
}
