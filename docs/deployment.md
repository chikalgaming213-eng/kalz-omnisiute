# Kalz OmniSuite — Automated Deployment Guide

**Audience:** operators, release engineers, and maintainers  
**Supported baseline:** Linux with Python 3.11 or newer  
**Deployment mode:** reproducible, secret-safe, plan-before-apply

## Deployment Contract

Deployment is a controlled state transition. The automation first validates the repository, creates an isolated virtual environment, installs pinned dependencies, compiles the package, runs tests, generates a release manifest, and only then installs or restarts services. A failed validation stops the process before a system change is made.

The deployment script is [`scripts/deploy.sh`](../scripts/deploy.sh). It supports `plan`, `apply`, `verify`, and `rollback` phases. `plan` is the default and does not modify system state. `apply` requires `KALZ_DEPLOY_APPROVED=true`, an explicit environment, and a release reference.

## Architecture Profiles

| Profile | Runtime | State | Recommended use |
|---|---|---|---|
| Workstation | CLI or PySide6 shell | Local SQLite and audit chain | Desktop administration |
| Single node | API, scheduler, worker, systemd | Local persistent directory | Small server |
| Distributed | Gateway, API replicas, workers, telemetry sink | Shared checkpoint and export storage | High-volume processing |
| Staged | Same as target with isolated namespace | Staging database and test secrets | Release verification |

## Prerequisites

The host must provide Python 3.11+, `git`, a compiler toolchain suitable for Python dependencies, and a service manager such as systemd for long-running deployment profiles. The operator must have a checkout of the intended commit and write access to the deployment directory. Root access is not required for plan or verify phases.

Create an environment file outside the repository. Never commit it:

```bash
export KALZ_ENV=staging
export KALZ_RELEASE=main
export KALZ_DEPLOY_APPROVED=false
export KALZ_DATA_DIR=/var/lib/kalz
export KALZ_CONFIG_DIR=/etc/kalz
export OPENAI_API_KEY="<rotated-key-if-needed>"
export OPENAI_MODEL="gpt-4.1-mini"
```

OpenAI credentials are optional for core operation. If enabled, the key must be injected by the host secret manager or environment. The deployment process validates that the variable exists but never prints its value.

## Quick Start: Plan First

```bash
./scripts/deploy.sh plan
```

The plan reports the detected Python version, repository revision, target environment, file paths, service units, dependency actions, and rollback location. It does not install packages, restart services, or call external AI APIs.

## Apply a Release

```bash
export KALZ_DEPLOY_APPROVED=true
export KALZ_ENV=staging
export KALZ_RELEASE=main
./scripts/deploy.sh apply
```

The apply phase performs the following sequence:

1. Verify the working tree and selected revision.
2. Create a timestamped release directory.
3. Create or reuse a virtual environment.
4. Install the project in editable or wheel mode according to profile.
5. Compile all Python modules.
6. Run the complete test suite.
7. Generate a release manifest and checksum.
8. Copy service templates and configuration references.
9. Create a pre-activation backup of local state.
10. Activate the release atomically.
11. Restart only the configured services.
12. Run health checks and record the deployment result.

The activation step must be atomic at the filesystem boundary. A failed health check returns the host to the previous release pointer and marks the deployment as failed.

## Verification

```bash
./scripts/deploy.sh verify
python -m compileall -q kalz
pytest -q
python -m kalz --doctor
```

Verification checks importability, test status, environment configuration, service reachability, audit directory writability, checkpoint integrity, and absence of accidental secret material in tracked files.

## Rollback

Rollback is available when a health check, smoke test, or operator review rejects the release:

```bash
./scripts/deploy.sh rollback
```

Rollback restores the previous release pointer and restarts affected services. It does not delete the failed release. Failed artifacts are retained for diagnosis until the configured retention policy removes them. A rollback must be accompanied by the deployment ID, failure phase, last known healthy revision, and relevant trace IDs.

## systemd Integration

A production host may run separate units for API, worker, scheduler, and telemetry export. Each unit should use a dedicated service account, a read-only application directory, a writable data directory, and an environment file readable only by the service account.

```ini
[Service]
User=kalz
Group=kalz
WorkingDirectory=/opt/kalz/current
EnvironmentFile=/etc/kalz/kalz.env
ExecStart=/opt/kalz/current/.venv/bin/python -m kalz --api
Restart=on-failure
RestartSec=5
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ReadWritePaths=/var/lib/kalz
```

The hardening directives are a baseline. Operators must test them against the selected Linux distribution and desktop integration requirements before production activation.

## Distributed Deployment Sequence

A distributed rollout should proceed in stages. First, deploy the checkpoint and export storage contract. Second, deploy the gateway without routing production traffic. Third, start one API replica and one worker. Fourth, run a synthetic request and a checkpoint recovery test. Fifth, add replicas gradually while observing latency, error rate, queue depth, and worker saturation. Finally, shift traffic by weighted routing.

The gateway must not send requests to a node that fails health checks. The load balancer should drain inflight work before a node is removed. A deployment is complete only after the new version has passed a full checkpoint round-trip and an observability export verification.

## CI/CD Pipeline

The repository workflow is [`../.github/workflows/deploy.yml`](../.github/workflows/deploy.yml). It separates test, package, and deployment jobs. Pull requests run compile and tests. Main-branch pushes create a manifest and package artifact. Environment deployment requires an explicit environment approval configured in GitHub and uses repository secrets only through masked environment variables.

| Stage | Trigger | Mutation | Required evidence |
|---|---|---|---|
| Test | Pull request or push | None | Compile, unit and integration tests |
| Package | Main push or tag | Artifact storage | Manifest, checksum, revision |
| Staging | Approved tag | Staging host | Smoke tests, health, traces |
| Production | Manual environment approval | Production host | Change ticket, backup, rollback target |

## Secret Management

Secrets must not be placed in `.env` files tracked by Git, shell command arguments, issue comments, CI logs, or generated documentation. Use a host secret manager, GitHub encrypted secrets, or an external vault. The application should receive only the specific secret required by the process. Rotate any credential that has appeared in chat, terminal output, logs, or an untrusted system.

## Operational Checklist

| Check | Plan | Apply | Verify | Rollback |
|---|---:|---:|---:|---:|
| Revision is pinned | yes | yes | yes | yes |
| Working tree is clean | yes | yes | yes | n/a |
| Tests pass | yes | yes | yes | before retry |
| Backup exists | report | required | verify | restore |
| Services restarted | no | controlled | inspect | controlled |
| Health checks pass | no | required | required | required |
| Audit record created | plan | required | inspect | required |
| Secret scan clean | required | required | required | required |

## Troubleshooting

If the deployment stops during dependency installation, preserve the release directory and inspect the generated manifest before retrying. If tests fail, do not bypass the gate; reproduce the failure in the same virtual environment. If a service starts but health checks fail, inspect structured logs by deployment ID and trace ID, then use rollback. If queue depth grows after rollout, reduce traffic weight, inspect worker capacity, and compare checkpoint age before adding workers.

## References

[1]: https://docs.python.org/3/library/venv.html "Python virtual environments"
[2]: https://docs.github.com/en/actions/deployment/about-deployments/deploying-with-github-actions "Deploying with GitHub Actions"
[3]: https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html "systemd service unit reference"
[4]: https://12factor.net/config "Configuration through environment"
