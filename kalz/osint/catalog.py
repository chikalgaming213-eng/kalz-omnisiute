from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class OSINTTool:
    name: str
    category: str
    repository: str
    url: str
    risk: str
    scope: str
    execution_mode: str = "plan-only"
    requires_consent: bool = True
    description: str = ""


_ENTRIES = (
    ("awesome-osint", "curated", "jivoi/awesome-osint"),
    ("awesome-osint-tools", "curated", "oryon-osint/awesome-osint-tools"),
    ("awesome_osint", "curated", "NCols/awesome_osint"),
    ("Sherlock", "identity", "sherlock-project/sherlock"),
    ("Maigret", "identity", "soxoj/maigret"),
    ("GHunt", "identity", "mxrch/GHunt"),
    ("PhoneInfoga", "identity", "sundowndev/phoneinfoga"),
    ("OWASP Amass", "domain-ip-recon", "OWASP/Amass"),
    ("Subfinder", "domain-ip-recon", "projectdiscovery/subfinder"),
    ("theHarvester", "domain-ip-recon", "laramies/theHarvester"),
    ("SpiderFoot", "domain-ip-recon", "smicallef/spiderfoot"),
    ("Recon-ng", "domain-ip-recon", "lanmaster53/recon-ng"),
    ("BBOT", "domain-ip-recon", "blacklanternsecurity/bbot"),
    ("Photon", "web-crawling", "s0md3v/Photon"),
    ("Crawl4AI", "web-crawling", "unclecode/crawl4ai"),
    ("Firecrawl", "web-crawling", "firecrawl/firecrawl"),
    ("MISP", "threat-intelligence", "MISP/MISP"),
    ("OpenCTI", "threat-intelligence", "OpenCTI-Platform/opencti"),
    ("Awesome Threat Intelligence", "threat-intelligence", "hslatman/awesome-threat-intelligence"),
)


def _build() -> tuple[OSINTTool, ...]:
    result = []
    for name, category, repository in _ENTRIES:
        risk = "high" if category in {"identity", "domain-ip-recon"} else "medium"
        result.append(OSINTTool(
            name=name,
            category=category,
            repository=repository,
            url=f"https://github.com/{repository}",
            risk=risk,
            scope="public sources only; user-authorized targets; no credential access",
            description=f"OSINT catalog entry sourced from {repository}",
        ))
    return tuple(result)


OSINT_TOOLS = _build()
OSINT_INDEX = {item.name.lower(): item for item in OSINT_TOOLS}


def osint_report() -> dict[str, Any]:
    categories: dict[str, int] = {}
    for item in OSINT_TOOLS:
        categories[item.category] = categories.get(item.category, 0) + 1
    return {"count": len(OSINT_TOOLS), "categories": categories, "tools": [asdict(item) for item in OSINT_TOOLS]}


def find_osint(name: str) -> OSINTTool | None:
    return OSINT_INDEX.get(name.strip().lower())
