import { useEffect, useState } from 'react'

export function useJsonStream<T>(url: string, initial: T[]) {
  const [entries, setEntries] = useState<T[]>(initial)
  useEffect(() => {
    const ws = new WebSocket(url)
    ws.onmessage = (e) => {
      try {
        const parsed = JSON.parse(e.data) as T
        setEntries((prev) => [...prev, parsed].slice(-400))
      } catch {
        // ignore invalid payload
      }
    }
    return () => ws.close()
  }, [url])
  return entries
}

export function useAuditStream() {
  return useJsonStream('ws://127.0.0.1:8000/ws/audit', [])
}

export function useGraphStream() {
  return useJsonStream('ws://127.0.0.1:8000/ws/graph', [])
}

export function useEventStream() {
  return useJsonStream('ws://127.0.0.1:8000/ws/events', [])
}
