from __future__ import annotations

import random
import uuid
from dataclasses import dataclass
from typing import Any


@dataclass
class IntegrationResult:
    ok: bool
    action_id: str
    message: str
    retries: int


class IntegrationAdapter:
    def __init__(self, name: str, failure_rate: float = 0.0, seed: int = 7):
        self.name = name
        self.failure_rate = failure_rate
        self.rng = random.Random(seed)

    def _run(self, action: str, employee: dict[str, Any], target: str) -> IntegrationResult:
        retries = 0
        while retries <= 2:
            failed = self.rng.random() < self.failure_rate
            if not failed:
                return IntegrationResult(
                    ok=True,
                    action_id=f"act_{uuid.uuid4().hex[:10]}",
                    message=f"{self.name}:{action}:{employee['id']}:{target}",
                    retries=retries,
                )
            retries += 1
        return IntegrationResult(
            ok=False,
            action_id=f"act_{uuid.uuid4().hex[:10]}",
            message=f"{self.name}:{action}:failed:{employee['id']}:{target}",
            retries=retries,
        )

    def provision_access(self, employee: dict[str, Any], app: str) -> dict[str, Any]:
        return self._run("provision_access", employee, app).__dict__

    def revoke_access(self, employee: dict[str, Any], app: str) -> dict[str, Any]:
        return self._run("revoke_access", employee, app).__dict__

    def invite_to_slack(self, employee: dict[str, Any]) -> dict[str, Any]:
        return self._run("invite_to_slack", employee, "slack").__dict__

    def provision_device(self, employee: dict[str, Any], device_type: str) -> dict[str, Any]:
        return self._run("provision_device", employee, device_type).__dict__

    def create_iam_user(self, employee: dict[str, Any]) -> dict[str, Any]:
        return self._run("create_iam_user", employee, "aws_iam").__dict__


class MockSlack(IntegrationAdapter):
    def __init__(self, failure_rate: float = 0.0, seed: int = 8):
        super().__init__("MockSlack", failure_rate, seed)


class MockGitHub(IntegrationAdapter):
    def __init__(self, failure_rate: float = 0.0, seed: int = 9):
        super().__init__("MockGitHub", failure_rate, seed)


class MockGoogleWorkspace(IntegrationAdapter):
    def __init__(self, failure_rate: float = 0.0, seed: int = 10):
        super().__init__("MockGoogleWorkspace", failure_rate, seed)


class MockOkta(IntegrationAdapter):
    def __init__(self, failure_rate: float = 0.0, seed: int = 11):
        super().__init__("MockOkta", failure_rate, seed)


class MockAWSIAM(IntegrationAdapter):
    def __init__(self, failure_rate: float = 0.0, seed: int = 12):
        super().__init__("MockAWSIAM", failure_rate, seed)
