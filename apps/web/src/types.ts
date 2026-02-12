export type NodeKind = 'EMPLOYEE' | 'DEVICE' | 'APPLICATION' | 'DEPARTMENT'
export type EdgeKind = 'REPORTS_TO' | 'ASSIGNED_TO' | 'HAS_ACCESS_TO' | 'MEMBER_OF'

export interface GraphNode { id: string; kind: NodeKind; display_name: string; attrs: Record<string, unknown> }
export interface GraphEdge { id: string; src: string; dst: string; kind: EdgeKind; attrs: Record<string, unknown> }
export interface GraphSnapshot { nodes: GraphNode[]; edges: GraphEdge[] }
export interface AuditEntry { id: string; ts: number; level: string; message: string; context: Record<string, unknown> }
