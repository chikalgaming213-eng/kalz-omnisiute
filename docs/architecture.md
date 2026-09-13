# Kalz OmniSuite — System Architecture

**Status:** Architecture baseline 1.0  
**Repository:** `chikalgaming213-eng/kalz-omnisiute`  
**Last updated:** 2026-09-14

## Executive Summary

Kalz OmniSuite is a native Linux operations platform organized as a layered Python runtime. The system combines a desktop shell, headless services, distributed data processing, machine-learning workflows, OpenAI integrations, observability, API routing, and layered defensive controls. Each layer exposes explicit contracts so that the desktop application, automation runner, distributed workers, and external integrations can evolve independently.

The architecture is **headless-first**. The CLI and service layers remain usable when Qt is unavailable. The graphical interface is an optional presentation layer that consumes the same domain services and policy decisions as the headless runtime.

> **Design principle:** privileged or consequential actions are planned, scoped, auditable, and reversible before execution. AI analysis can recommend actions, but it does not bypass policy enforcement.

## Architecture at a Glance

![Kalz OmniSuite 3D architecture](diagrams/system-architecture.svg)

The source diagram is available at [`diagrams/system-architecture.d2`](diagrams/system-architecture.d2). It models the system as an isometric stack: user surfaces at the top, orchestration and intelligence in the middle, data and security planes below, and operating-system adapters at the foundation.

## Layer Model

| Layer | Primary modules | Responsibility | Trust boundary |
|---|---|---|---|
| Presentation | `kalz/app.py`, `kalz/ui/`, `kalz/cli.py` | Qt/QML desktop shell, headless CLI, user-facing status | User process |
| API and edge | `kalz/api/`, `kalz/gateway/` | REST contracts, validation, routing, backend selection, load balancing | Network boundary |
| Orchestration | `kalz/core/`, `kalz/automation/` | Jobs, workflows, process lifecycle, scheduling, retries, rollback planning | Application control plane |
| Intelligence | `kalz/ml/`, `kalz/integrations/`, `kalz/observability/llm_analysis.py` | Feature processing, model lifecycle, inference, LLM-assisted log analysis | External-model boundary |
| Distributed data | `kalz/distributed/` | Partitioning, shuffle, workers, checkpoints, pipeline stages | Worker/data-plane boundary |
| Observability | `kalz/observability/` | Metrics, structured logs, traces, alerts, export, retention | Telemetry boundary |
| Security | `kalz/security/`, `kalz/securityx/`, `kalz/defense/` | Audit, scope, keys, AEAD, secure channels, access, defense and hardening | Security control plane |
| Persistence | `kalz/db/`, audit files, backup services | SQLite state, audit chain, reports, snapshots | Local data boundary |
| Platform | `kalz/platform/`, `kalz/de_integration/`, `kalz/system/` | Linux distro, desktop environment, package and system adapters | Operating-system boundary |

## Runtime Flows

### Interactive desktop flow

The desktop starts the application bootstrap and resolves a platform profile. View models call domain services rather than shell commands directly. A requested operation is converted into a scoped plan. The policy layer evaluates consent, mode, capability, and target scope. The audit chain records the plan and result. The UI receives events through the application event bus and displays health, progress, and failure recovery options.

### Headless API flow

A request enters through the REST handler or gateway. Validation rejects malformed input before the request reaches a workflow. The gateway selects a healthy backend and attaches a request identifier. The workflow engine constructs an operation plan. The security layer evaluates the principal, scope, and capability. The runner executes only an approved plan. Structured logs and metrics are emitted throughout the lifecycle.

### Distributed processing flow

Input records are partitioned by deterministic key assignment. Partition batches move through shuffle and aggregation stages. Workers lease tasks from a bounded queue. Backpressure prevents unbounded memory growth. Checkpoints capture offsets and lineage. A failed stage produces a recovery plan from the latest valid checkpoint rather than silently replaying unknown state.

### LLM observability flow

The log analysis service selects a bounded event window from the distributed log store. Sensitive fields are redacted before prompt construction. The OpenAI Agent receives only the approved analysis tool set. The agent produces a diagnostic response; it cannot directly execute privileged remediation. If the Agents SDK or API is unavailable, the service returns a deterministic local summary based on error counts and trace correlation.

## Security and Trust Boundaries

The system treats every boundary as hostile until explicitly validated. Network requests are validated at the API edge. Backend routing does not imply authorization. Authorization is evaluated separately by capability and scope policy. Secrets are loaded from environment or encrypted storage and are never embedded in source files.

The OpenAI integration is an external trust boundary. Prompts are bounded and redacted. Responses are treated as untrusted text. Agent tools are allowlisted by name. An LLM recommendation is advisory and must pass the same policy path as any human-requested operation.

The distributed worker plane is an execution boundary. Workers receive typed task payloads, bounded retries, and checkpoint metadata. A worker failure must be visible through metrics, logs, and alerts. No worker may widen its own scope.

## Data Contracts

| Contract | Producer | Consumer | Required invariants |
|---|---|---|---|
| `OperationContext` | Workflow/CLI/API | Automation engine | Non-empty operation ID; explicit mode; target scope |
| `SecurityDecision` | Security engine | Runner/API/UI | Boolean decision; reason; risk; evidence |
| `Record` / `Partition` | Distributed input | Shuffle/worker | Stable key; deterministic partition; checksum |
| `Checkpoint` | Pipeline stage | Recovery planner | Stage, offsets, checksum, lineage |
| `LogEvent` | Runtime services | Log store/LLM analyzer | Structured level, service, event ID, redaction support |
| `MetricSample` | Runtime services | Aggregator/exporter | Name, numeric value, timestamp, labels |
| `InferenceRequest` | ML client | Inference server | Request ID, model identity, feature vector |

## Failure Strategy

Failures are classified as validation, policy, dependency, capacity, execution, or integrity failures. Validation failures stop at the boundary. Policy failures are denied and audited. Dependency failures use bounded retry with exponential backoff. Capacity failures activate backpressure. Execution failures produce a failed task and recovery metadata. Integrity failures stop the affected flow and require operator review.

The system prefers **fail closed** for authorization, key validity, scope, and integrity. It may fail open only for non-critical telemetry delivery when the configured policy explicitly permits local buffering.

## Deployment Topology

The smallest deployment is a single Linux host running the CLI, local SQLite state, audit chain, and optional desktop UI. A larger deployment separates the edge gateway, API service, worker pool, observability exporter, and persistent storage. The same Python package is used in both topologies; only process configuration and service boundaries change.

| Profile | Processes | Suitable for |
|---|---|---|
| Desktop | GUI plus local headless services | Individual workstation operations |
| Single-node server | API, scheduler, worker, SQLite | Small controlled environments |
| Distributed | Gateway, API replicas, workers, checkpoint store, telemetry sink | High-volume processing |
| Lab/digital twin | Distributed profile plus simulation and replay controls | Non-production experimentation |

## Operational Invariants

1. A privileged operation must have a plan, scope, consent state, and audit record before execution.
2. A failed distributed stage must not be acknowledged without a checkpoint or an explicit operator decision.
3. Secrets must enter through environment, a secret manager, or encrypted storage; they must not enter Git.
4. Every externally visible request must have a request or trace identifier.
5. LLM output is advisory and cannot directly bypass the security or approval layers.
6. Deployment must be reproducible from a tagged commit and a recorded Python dependency set.

## References

[1]: https://docs.python.org/3/library/venv.html "Python virtual environments"
[2]: https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html "systemd service units"
[3]: https://docs.github.com/en/actions "GitHub Actions documentation"
[4]: https://platform.openai.com/docs/ "OpenAI platform documentation"
