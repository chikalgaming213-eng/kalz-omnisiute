.PHONY: help bootstrap install verify test doctor registry osint gui api deploy-plan package-plan clean

PYTHON ?= python3

help:
	@printf '%s\n' 'Kalz OmniSuite developer targets:'
	@printf '%s\n' '  make bootstrap    plan-only bootstrap summary'
	@printf '%s\n' '  make install      create .venv and install test extras (approval required)'
	@printf '%s\n' '  make verify       run complete read-only quality gate'
	@printf '%s\n' '  make test         run pytest'
	@printf '%s\n' '  make doctor       inspect distro and desktop environment'
	@printf '%s\n' '  make registry     print tool registry JSON'
	@printf '%s\n' '  make osint        print OSINT catalog JSON'
	@printf '%s\n' '  make gui          start native GUI'
	@printf '%s\n' '  make api          start local REST API'
	@printf '%s\n' '  make deploy-plan  show deployment plan'
	@printf '%s\n' '  make package-plan show package build plan'

bootstrap:
	./scripts/bootstrap.sh plan

install:
	KALZ_BOOTSTRAP_APPROVED=true ./scripts/bootstrap.sh apply

verify:
	./scripts/verify.sh

test:
	$(PYTHON) -m pytest -q

doctor:
	$(PYTHON) -m kalz --doctor

registry:
	$(PYTHON) -m kalz --registry

osint:
	$(PYTHON) -m kalz --osint

gui:
	$(PYTHON) -m kalz --gui

api:
	$(PYTHON) -m kalz --api

deploy-plan:
	./scripts/deploy.sh plan

package-plan:
	./scripts/build_deb.sh
	./scripts/build_rpm.sh
	./scripts/build_appimage.sh
	./scripts/build_flatpak.sh

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -rf .pytest_cache build dist *.egg-info
