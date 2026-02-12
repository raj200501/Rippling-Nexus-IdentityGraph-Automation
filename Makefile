.PHONY: bootstrap verify demo loc

bootstrap:
	python -m venv .venv
	@echo "Bootstrap complete (offline-friendly)."

verify:
	bash scripts/verify.sh

demo:
	bash scripts/dev.sh

loc:
	. .venv/bin/activate && python scripts/loc.py
