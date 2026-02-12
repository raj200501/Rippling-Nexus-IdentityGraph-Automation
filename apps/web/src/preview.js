const links = [
  ['/', 'Home'],
  ['/org-graph', 'Org Graph'],
  ['/people', 'People Directory'],
  ['/access', 'Access Matrix']
]

const root = document.getElementById('root')

function diagnosticsContent() {
  return `
    <ul>
      <li>Commit SHA: ${window.__COMMIT_SHA__ ?? 'local-dev'}</li>
      <li>Mode: ${location.hostname === 'localhost' ? 'development' : 'preview'}</li>
      <li>WS Status: offline (mock mode)</li>
      <li>Last Error: none</li>
    </ul>
  `
}

function homeContent() {
  return `
    <h1>Nexus Identity Graph</h1>
    <section class="boot-panel"><strong>Boot OK</strong><p>UI shell rendered using local fallback widgets.</p></section>
    <section class="widget-grid">
      <article class="card"><h2>Identities</h2><p class="metric-value">1,248</p><small>Mock dataset loaded</small></article>
      <article class="card"><h2>Workflows</h2><p class="metric-value">14 active</p><small>Scheduler healthy</small></article>
      <article class="card"><h2>Alerts</h2><p class="metric-value">2 warning</p><small>Backend optional</small></article>
    </section>
    <section class="card diagnostics"><h2>Preview Diagnostics</h2>${diagnosticsContent()}</section>
  `
}

function routeContent(path) {
  if (path === '/' || path === '') return homeContent()
  const found = links.find(([to]) => to === path)
  if (!found) return homeContent()
  return `<h1>${found[1]}</h1><section class="card"><p>This route is online and rendering safely.</p></section>`
}

function render(pathname = location.pathname) {
  const nav = links.map(([to, label]) => `<a href="${to}" data-link>${label}</a>`).join('')
  root.innerHTML = `<div class="layout"><nav aria-label="Primary navigation">${nav}</nav><main>${routeContent(pathname)}</main></div>`
}

document.addEventListener('click', (event) => {
  const link = event.target.closest('a[data-link]')
  if (!link) return
  event.preventDefault()
  const href = link.getAttribute('href')
  history.pushState({}, '', href)
  render(href)
})

window.addEventListener('popstate', () => render())
render()
