# Rippling-Nexus-IdentityGraph-Automation

Nexus — Unified Identity Graph + IT Automation Control Plane.

## Quickstart (60s)
1. `make bootstrap`
2. `make verify`
3. `make demo`
4. Open `http://127.0.0.1:5173`

## Make targets
- `make bootstrap` install python/node deps
- `make verify` lint + tests + build + coverage gate
- `make demo` run api + web + simulator
- `make loc` report line counts

## Interview mode bullets
- Graph-first model enables reachability queries and policy explainability.
- Deterministic simulator makes reproductions easy in debugging.
- Workflow engine supports dry-run and idempotent automation actions.
- Cycle prevention and repair maintain manager hierarchy integrity.
- Streaming UI reflects audit and graph updates with queue backpressure.
