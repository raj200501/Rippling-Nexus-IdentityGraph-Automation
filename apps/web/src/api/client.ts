import { z } from 'zod'
import type { GraphSnapshot, AuditEntry } from '../types'

const graphSchema = z.object({ nodes: z.array(z.any()), edges: z.array(z.any()) })
const auditSchema = z.array(z.any())

const API = import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000'

export async function getGraph(): Promise<GraphSnapshot> {
  const res = await fetch(`${API}/graph`)
  const json = await res.json()
  return graphSchema.parse(json) as GraphSnapshot
}

export async function getAudit(): Promise<AuditEntry[]> {
  const res = await fetch(`${API}/audit`)
  return auditSchema.parse(await res.json()) as AuditEntry[]
}

export async function runQuery(payload: unknown) {
  const res = await fetch(`${API}/query`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
  return res.json()
}

export async function hireEmployee(payload: Record<string, unknown>) {
  const res = await fetch(`${API}/mutations/hire`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
  return res.json()
}
