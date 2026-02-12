import type { PropsWithChildren, ReactNode } from 'react'

export function Button({ children, onClick }: PropsWithChildren<{ onClick?: () => void }>) {
  return <button className="ui-button" onClick={onClick}>{children}</button>
}

export function Card({ title, children }: PropsWithChildren<{ title?: ReactNode }>) {
  return <section className="ui-card"><header>{title}</header><div>{children}</div></section>
}

export function Badge({ children }: PropsWithChildren) { return <span className="ui-badge">{children}</span> }
export function Table({ children }: PropsWithChildren) { return <table className="ui-table">{children}</table> }
export function Drawer({ open, children }: PropsWithChildren<{ open: boolean }>) { return open ? <aside className="ui-drawer">{children}</aside> : null }
export function Modal({ open, children }: PropsWithChildren<{ open: boolean }>) { return open ? <div className="ui-modal">{children}</div> : null }
export function Skeleton() { return <div className="ui-skeleton" /> }
export function CodeBlock({ code }: { code: string }) { return <pre className="ui-code">{code}</pre> }
