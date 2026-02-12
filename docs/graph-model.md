# Graph Model
Nodes and edges are persisted in SQLite and loaded into a NetworkX MultiDiGraph.
Includes cycle detection for `REPORTS_TO` and repair logic on manager termination.
