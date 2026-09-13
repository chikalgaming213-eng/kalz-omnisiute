# Kalz OmniSuite Full-Stack Developer Guide

## Runtime layers

The desktop shell is PySide6/QML/QSS and is optional at import time. The CLI and local HTTP API remain usable without a display. Domain services are plain Python: `SecureRunner` handles argv-based subprocesses, `WorkflowEngine` composes steps, `Database` persists jobs and reports, `AuditChain` records tamper-evident events, and `Scheduler` handles recurring async callbacks.

## Running the stack

```bash
PYTHONPATH=. python -m kalz --doctor
PYTHONPATH=. python -m kalz --registry
PYTHONPATH=. python -m kalz --api
PYTHONPATH=. python -m kalz --gui
pytest -q
```

The API is localhost-only by default. `/health` verifies liveness, `/api/v1/profile` returns the detected distro and DE, and `/api/v1/plan` returns a validated dry-run plan. Network exposure, privileged actions, package-source changes, and release signing require an explicit production policy and host-specific verification.

## Extension points

Add a tool by extending the registry metadata and then providing a typed adapter, parser, fixture, and integration test. Add a desktop environment by implementing `BaseDEAdapter`, registering it in `factory.py`, and testing the capability probe on a real session. Add a workflow by composing `WorkflowStep` values and keeping every step auditable and cancellable. Add a plugin through `PluginManifest` and `PluginRegistry`; plugins must declare capabilities and must not receive implicit privileged access.

## Failure model

Failures stop the current workflow, preserve audit records, return diagnostics, and leave user data intact. No failure path wipes, deletes, or damages the host.
