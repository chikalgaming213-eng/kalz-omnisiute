# Kalz OmniSuite Documentation

Dokumentasi ini menjadi pintu masuk untuk memahami arsitektur dan mengoperasikan Kalz OmniSuite.

| Dokumen | Isi |
|---|---|
| [Architecture](architecture.md) | Layer sistem, trust boundaries, data flows, failure strategy, dan topology |
| [Deployment](deployment.md) | Plan/apply/verify/rollback, CI/CD, secrets, systemd, dan distributed rollout |
| [Architecture Diagram](diagrams/system-architecture.svg) | Diagram arsitektur 3D/isometrik |
| [D2 Source](diagrams/system-architecture.d2) | Source diagram yang dapat diedit |
| [Developer Guide](developer-guide.md) | Konvensi runtime dan lapisan pengembangan |
| [OpenAPI](openapi.json) | Contract endpoint REST |
| [OSINT Catalog](osint.md) | Sources, plan-only adapters, scope, consent, and GUI coverage |

## Operational Entry Points

```bash
./scripts/deploy.sh plan
./scripts/deploy.sh verify
pytest -q
python -m kalz --doctor
```

Deployment default adalah **plan-only**. Perubahan host membutuhkan `KALZ_DEPLOY_APPROVED=true` dan harus dijalankan melalui prosedur staging atau environment approval.
