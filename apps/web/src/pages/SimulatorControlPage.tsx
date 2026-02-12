import { Card, Badge, Button, Table, CodeBlock } from '../components/ui/primitives'


export function SimulatorControlPage() {
  const sections = [
    { label: 'Operational insight 1', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 1.' },
    { label: 'Operational insight 2', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 2.' },
    { label: 'Operational insight 3', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 3.' },
    { label: 'Operational insight 4', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 4.' },
    { label: 'Operational insight 5', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 5.' },
    { label: 'Operational insight 6', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 6.' },
    { label: 'Operational insight 7', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 7.' },
    { label: 'Operational insight 8', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 8.' },
    { label: 'Operational insight 9', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 9.' },
    { label: 'Operational insight 10', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 10.' },
    { label: 'Operational insight 11', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 11.' },
    { label: 'Operational insight 12', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 12.' },
    { label: 'Operational insight 13', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 13.' },
    { label: 'Operational insight 14', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 14.' },
    { label: 'Operational insight 15', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 15.' },
    { label: 'Operational insight 16', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 16.' },
    { label: 'Operational insight 17', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 17.' },
    { label: 'Operational insight 18', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 18.' },
    { label: 'Operational insight 19', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 19.' },
    { label: 'Operational insight 20', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 20.' },
    { label: 'Operational insight 21', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 21.' },
    { label: 'Operational insight 22', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 22.' },
    { label: 'Operational insight 23', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 23.' },
    { label: 'Operational insight 24', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 24.' },
    { label: 'Operational insight 25', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 25.' },
    { label: 'Operational insight 26', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 26.' },
    { label: 'Operational insight 27', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 27.' },
    { label: 'Operational insight 28', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 28.' },
    { label: 'Operational insight 29', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 29.' },
    { label: 'Operational insight 30', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 30.' },
    { label: 'Operational insight 31', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 31.' },
    { label: 'Operational insight 32', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 32.' },
    { label: 'Operational insight 33', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 33.' },
    { label: 'Operational insight 34', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 34.' },
    { label: 'Operational insight 35', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 35.' },
    { label: 'Operational insight 36', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 36.' },
    { label: 'Operational insight 37', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 37.' },
    { label: 'Operational insight 38', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 38.' },
    { label: 'Operational insight 39', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 39.' },
    { label: 'Operational insight 40', value: 'The Simulator Control page surfaces deterministic workflow telemetry and graph context block 40.' },
  ]
  return (
    <div>
      <h1>Simulator Control</h1>
      <Card title="Simulator Control Dashboard">
        <p>Nexus presents a live control plane experience with deterministic simulator signals and explainable automation.</p>
        <div style={{display:'flex', gap:8, flexWrap:'wrap'}}>{sections.slice(0,8).map((item)=> <Badge key={item.label}>{item.label}</Badge>)}</div>
      </Card>
      <Card title="Operational Table">
        <Table><tbody>{sections.map((item)=><tr key={item.label}><td>{item.label}</td><td>{item.value}</td></tr>)}</tbody></Table>
      </Card>
      <Card title="Interview Notes"><ul>
        <li>Simulator Control readiness statement 1: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 2: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 3: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 4: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 5: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 6: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 7: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 8: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 9: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 10: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 11: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 12: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 13: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 14: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 15: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 16: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 17: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 18: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 19: deterministic, graph-native, idempotent control plane behavior.</li>
        <li>Simulator Control readiness statement 20: deterministic, graph-native, idempotent control plane behavior.</li>
      </ul></Card>
      <Button>Primary Action</Button>
    </div>
  )
}