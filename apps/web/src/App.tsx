import { Link, Route, Routes } from 'react-router-dom'
import { OrgGraphPage } from './pages/OrgGraphPage'
import { PeopleDirectoryPage } from './pages/PeopleDirectoryPage'
import { AccessMatrixPage } from './pages/AccessMatrixPage'
import { DevicesInventoryPage } from './pages/DevicesInventoryPage'
import { AuditLogPage } from './pages/AuditLogPage'
import { WorkflowRunsPage } from './pages/WorkflowRunsPage'
import { GraphQueriesPage } from './pages/GraphQueriesPage'
import { OrgHealthPage } from './pages/OrgHealthPage'
import { ChangeTimelinePage } from './pages/ChangeTimelinePage'
import { IntegrationsPage } from './pages/IntegrationsPage'
import { SimulatorControlPage } from './pages/SimulatorControlPage'
import { SettingsPage } from './pages/SettingsPage'

const links = [
  ['/', 'Org Graph'],
  ['/people', 'People Directory'],
  ['/access', 'Access Matrix'],
  ['/devices', 'Devices Inventory'],
  ['/audit', 'Audit Log'],
  ['/workflows', 'Workflow Runs'],
  ['/queries', 'Graph Queries'],
  ['/health', 'Org Health'],
  ['/timeline', 'Change Timeline'],
  ['/integrations', 'Integrations'],
  ['/simulator', 'Simulator Control'],
  ['/settings', 'Settings']
]

export function App() {
  return (
    <div className="layout">
      <nav>{links.map(([to, label]) => <Link key={to} to={to}>{label}</Link>)}</nav>
      <main>
        <Routes>
          <Route path="/" element={<OrgGraphPage />} />
          <Route path="/people" element={<PeopleDirectoryPage />} />
          <Route path="/access" element={<AccessMatrixPage />} />
          <Route path="/devices" element={<DevicesInventoryPage />} />
          <Route path="/audit" element={<AuditLogPage />} />
          <Route path="/workflows" element={<WorkflowRunsPage />} />
          <Route path="/queries" element={<GraphQueriesPage />} />
          <Route path="/health" element={<OrgHealthPage />} />
          <Route path="/timeline" element={<ChangeTimelinePage />} />
          <Route path="/integrations" element={<IntegrationsPage />} />
          <Route path="/simulator" element={<SimulatorControlPage />} />
          <Route path="/settings" element={<SettingsPage />} />
        </Routes>
      </main>
    </div>
  )
}
