from __future__ import annotations

import argparse
import random
import time

import httpx

DEPARTMENTS = ["Engineering", "Sales", "IT", "Finance"]
ROLES = ["Software Engineer", "Sales Executive", "IT Admin", "Finance Analyst"]


def run(seed: int, interval: float, max_events: int, api_url: str = "http://127.0.0.1:8000") -> None:
    rng = random.Random(seed)
    with httpx.Client(timeout=5.0) as client:
        for i in range(max_events):
            graph = client.get(f"{api_url}/graph").json()
            employees = [n for n in graph["nodes"] if n["kind"] == "EMPLOYEE"]
            manager = rng.choice(employees)
            name = f"Auto Hire {i}"
            department = rng.choice(DEPARTMENTS)
            role = ROLES[DEPARTMENTS.index(department)]
            client.post(
                f"{api_url}/mutations/hire",
                json={"name": name, "department": department, "role": role, "manager_id": manager["id"]},
            )
            if i % 5 == 0 and len(employees) > 5:
                target = rng.choice(employees[1:])
                client.post(f"{api_url}/mutations/terminate", json={"employee_id": target["id"]})
            if i % 7 == 0 and len(employees) > 2:
                a = rng.choice(employees)
                b = rng.choice(employees)
                client.post(f"{api_url}/mutations/reassign", json={"employee_id": a["id"], "new_manager_id": b["id"]})
            time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--interval", type=float, default=2.0)
    parser.add_argument("--max", type=int, default=200)
    args = parser.parse_args()
    run(args.seed, args.interval, args.max)
