const base = import.meta.env.BASE_URL.replace(/\/$/, '');

export function url(path: string): string {
  return `${base}${path}`;
}

export function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
}

export function getAllTactics(loobins: any[]): Map<string, number> {
  const counts = new Map<string, number>();
  for (const loobin of loobins) {
    for (const uc of loobin.data.example_use_cases) {
      for (const tactic of uc.tactics ?? []) {
        counts.set(tactic, (counts.get(tactic) ?? 0) + 1);
      }
    }
  }
  return new Map([...counts.entries()].sort((a, b) => a[0].localeCompare(b[0])));
}

export function getAllTags(loobins: any[]): Map<string, number> {
  const counts = new Map<string, number>();
  for (const loobin of loobins) {
    for (const uc of loobin.data.example_use_cases) {
      for (const tag of uc.tags ?? []) {
        counts.set(tag, (counts.get(tag) ?? 0) + 1);
      }
    }
  }
  return new Map([...counts.entries()].sort((a, b) => a[0].localeCompare(b[0])));
}

export function loobinHasTactic(loobin: any, tactic: string): boolean {
  return loobin.data.example_use_cases.some((uc: any) =>
    (uc.tactics ?? []).includes(tactic)
  );
}

export function loobinHasTag(loobin: any, tag: string): boolean {
  return loobin.data.example_use_cases.some((uc: any) =>
    (uc.tags ?? []).includes(tag)
  );
}

export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}

const tacticColors: Record<string, string> = {
  'Reconnaissance': 'bg-blue-600',
  'Resource Development': 'bg-indigo-600',
  'Initial Access': 'bg-violet-600',
  'Execution': 'bg-red-600',
  'Persistence': 'bg-orange-600',
  'Privilege Escalation': 'bg-amber-600',
  'Defense Evasion': 'bg-yellow-600',
  'Credential Access': 'bg-lime-600',
  'Discovery': 'bg-green-600',
  'Lateral Movement': 'bg-emerald-600',
  'Collection': 'bg-teal-600',
  'Exfiltration': 'bg-cyan-600',
  'Command and Control': 'bg-sky-600',
  'Impact': 'bg-rose-600',
};

export function tacticColor(tactic: string): string {
  return tacticColors[tactic] ?? 'bg-slate-600';
}
