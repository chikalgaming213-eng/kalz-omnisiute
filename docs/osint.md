# OSINT Catalog and Safe Execution Policy

Kalz OmniSuite now catalogs the public OSINT repositories supplied for this project. The catalog covers curated OSINT lists, identity/username discovery, domain and IP reconnaissance, web crawling, and threat-intelligence platforms.

## Cataloged Sources

| Category | Sources |
|---|---|
| Curated | `jivoi/awesome-osint`, `oryon-osint/awesome-osint-tools`, `NCols/awesome_osint` |
| Identity | Sherlock, Maigret, GHunt, PhoneInfoga |
| Domain/IP/recon | OWASP Amass, Subfinder, theHarvester, SpiderFoot, Recon-ng, BBOT |
| Web crawling | Photon, Crawl4AI, Firecrawl |
| Threat intelligence | MISP, OpenCTI, Awesome Threat Intelligence |

The implementation is in [`kalz/osint/catalog.py`](../kalz/osint/catalog.py). Each entry contains a source repository, URL, category, risk, authorized scope, consent requirement, and execution mode.

## Safety Contract

The catalog is declarative. It does not install or invoke third-party OSINT binaries automatically. The planner is plan-only and requires explicit consent before any future execution adapter can run. Local, loopback, file, and Unix-socket targets are rejected. The intended scope is public sources and user-authorized targets only.

```bash
python -m kalz --osint
```

The command returns the catalog as JSON. A future adapter must first produce an audit record, validate scope, redact sensitive output, and pass the same security policy used by other Kalz operations.

## GUI Coverage

The native dashboard includes an **OSINT Catalog** card alongside system health, tool registry, automation, and audit chain. The card is informational and does not grant direct execution privileges. This keeps the GUI consistent with the preview-first and consent-gated operating model.

## References

[1]: https://github.com/jivoi/awesome-osint "Awesome OSINT curated list"
[2]: https://github.com/sherlock-project/sherlock "Sherlock username investigation tool"
[3]: https://github.com/OWASP/Amass "OWASP Amass attack surface mapping"
[4]: https://github.com/MISP/MISP "MISP threat intelligence platform"
[5]: https://github.com/OpenCTI-Platform/opencti "OpenCTI cyber threat intelligence platform"
