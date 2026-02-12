.PHONY: bootstrap verify demo loc

bootstrap:
	python -m venv .venv
	npm install --no-audit --no-fund --prefix apps/web
	@echo "Bootstrap complete."

verify:
	bash scripts/verify.sh

demo:
	bash scripts/dev.sh

loc:
	. .venv/bin/activate && python scripts/loc.py
