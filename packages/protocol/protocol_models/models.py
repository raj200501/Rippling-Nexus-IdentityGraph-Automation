from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class Node(BaseModel):
    id: str
    kind: Literal["EMPLOYEE", "DEVICE", "APPLICATION", "DEPARTMENT"]
    display_name: str
    attrs: dict[str, Any] = Field(default_factory=dict)


class Edge(BaseModel):
    id: str
    src: str
    dst: str
    kind: Literal["REPORTS_TO", "ASSIGNED_TO", "HAS_ACCESS_TO", "MEMBER_OF"]
    attrs: dict[str, Any] = Field(default_factory=dict)


class Event(BaseModel):
    id: str
    ts: int
    type: str
    payload: dict[str, Any]


class AuditEntry(BaseModel):
    id: str
    ts: int
    level: Literal["INFO", "WARN", "ERROR"] = "INFO"
    message: str
    context: dict[str, Any] = Field(default_factory=dict)


class WorkflowRun(BaseModel):
    id: str
    ts: int
    event_id: str
    status: Literal["running", "success", "failed", "dry-run"]
    details: dict[str, Any] = Field(default_factory=dict)


class GraphSnapshot(BaseModel):
    nodes: list[Node]
    edges: list[Edge]


class GraphQuery(BaseModel):
    select: str = "EMPLOYEE"
    where: dict[str, Any] = Field(default_factory=dict)
    constraints: list[dict[str, Any]] = Field(default_factory=list)


class GraphMutation(BaseModel):
    nodes: list[Node] = Field(default_factory=list)
    edges: list[Edge] = Field(default_factory=list)
