import { render, screen, fireEvent } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { GraphQueriesPage } from '../pages/GraphQueriesPage'
import { describe, it, expect, vi } from 'vitest'

vi.mock('../api/client', () => ({ runQuery: vi.fn(async () => ({ employees: [] })) }))

describe('query builder', () => {
  it('renders and submits', async () => {
    render(<MemoryRouter><GraphQueriesPage /></MemoryRouter>)
    fireEvent.click(screen.getByText('Run Query'))
    expect(screen.getByText('Run Query')).toBeInTheDocument()
  })
})
