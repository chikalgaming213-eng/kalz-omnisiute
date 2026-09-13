# Code Review — 2026-09-14

## Summary
Intent: deliver a native Linux full-stack Kalz OmniSuite with automation, API, desktop UI, packaging, and 200+ tool metadata. The review found an input-validation gap in the plan API and placeholder-only shell pipelines; both were corrected in this revision.

## Critical issues

No unresolved critical issues remain in the reviewed paths. The API now rejects malformed package lists, limits request size, and never interpolates package input into a shell command. The secure runner continues to use argv-based subprocess creation and defaults to dry-run.

## Major issues

The QML surface is a runnable dashboard shell rather than the complete operational workspace described by the blueprint. Package execution, DE mutation, WebSocket streaming, and production signing remain explicit future layers. They must not be described as complete until tested on representative KDE, XFCE, and GNOME hosts.

The registry contains 294 metadata entries, but metadata presence does not mean every binary has a dedicated parser or workflow implementation. The next milestone is to add typed adapters and fixtures per category.

## Minor issues

Formatting is compact in a few standard-library modules and should be normalized with Ruff when the dependency is added to CI. API authentication is intentionally not enabled for localhost development; any network exposure requires authentication, TLS, and an allowlist before release.

## Positive feedback

The project uses a headless-first architecture, SQLite persistence, async event delivery, an audit hash-chain, explicit plugin manifests, DE capability detection, and tests that do not require root or a real graphical session. The failure model is non-destructive and reviewable.

## Verification

```text
python -m compileall -q kalz tests scripts       PASS
pytest -q                                         4 passed
kalz --doctor                                     PASS
scripts/detect_de.sh                              PASS
scripts/build_deb.sh                              PASS (plan-only)
scripts/sign_release.sh                            PASS (plan-only)
placeholder pipeline search                       PASS (none)
git diff --check                                  PASS
```

## Verdict

**Comment / Request Changes for production release.** The full-stack foundation is runnable and the reviewed blockers are fixed, but production claims for all tool workflows, native packaging, privileged mutation, and full DE UI integration require additional implementation and host-matrix verification.
