import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const tactics = [
  'Reconnaissance',
  'Resource Development',
  'Initial Access',
  'Execution',
  'Persistence',
  'Privilege Escalation',
  'Defense Evasion',
  'Credential Access',
  'Discovery',
  'Lateral Movement',
  'Collection',
  'Exfiltration',
  'Command and Control',
  'Impact',
] as const;

const loobins = defineCollection({
  loader: glob({ pattern: '*.yml', base: '../LOOBins' }),
  schema: z.object({
    name: z.string(),
    author: z.string(),
    short_description: z.string(),
    full_description: z.string(),
    created: z.coerce.date(),
    example_use_cases: z.array(
      z.object({
        name: z.string(),
        description: z.string(),
        code: z.string().optional(),
        tactics: z.array(z.enum(tactics)).optional().default([]),
        tags: z.array(z.string()).optional().default([]),
      })
    ),
    paths: z.array(z.string()),
    detections: z.array(
      z.object({
        name: z.string(),
        url: z.string(),
      })
    ),
    resources: z
      .array(
        z.object({
          name: z.string(),
          url: z.string(),
        })
      )
      .optional()
      .default([]),
    acknowledgements: z.array(z.string()).optional().default([]),
  }),
});

export const collections = { loobins };
