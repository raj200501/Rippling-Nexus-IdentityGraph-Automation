from pathlib import Path

ROOT = Path('.')

def count(path: Path) -> int:
    total = 0
    for p in path.rglob('*'):
        if p.is_file() and p.suffix in {'.py', '.ts', '.tsx', '.css', '.md', '.sh', '.yml', '.yaml'}:
            total += len(p.read_text().splitlines())
    return total

for key in [Path('apps/web/src'), Path('apps/api'), Path('packages'), Path('.')]:
    if key.exists():
        print(f"{key}: {count(key)}")
