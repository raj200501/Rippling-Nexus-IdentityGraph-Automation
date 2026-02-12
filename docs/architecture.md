# Architecture

```mermaid
flowchart LR
  Simulator --> API
  API --> Graph[(SQLite + NetworkX)]
  API --> Workflows
  Workflows --> Integrations
  API --> WebsocketStreams
  Web --> WebsocketStreams
```
