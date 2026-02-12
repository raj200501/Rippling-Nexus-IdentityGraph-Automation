import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { App } from '../App'
import { describe, it, expect } from 'vitest'

const routes = ['/', '/people', '/access', '/devices', '/audit', '/workflows', '/queries', '/health', '/timeline', '/integrations', '/simulator', '/settings']

describe('routes', () => {
  routes.forEach((route) => {
    it(`renders ${route}`, () => {
      render(<MemoryRouter initialEntries={[route]}><App /></MemoryRouter>)
      expect(screen.getByRole('heading')).toBeInTheDocument()
    })
  })
})
