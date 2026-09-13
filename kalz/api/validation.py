from __future__ import annotations

import re

PACKAGE_RE = re.compile(r'^[A-Za-z0-9][A-Za-z0-9.+_-]{0,127}$')

class APIInputError(ValueError):
    pass

def validate_packages(value: object) -> list[str]:
    if not isinstance(value, list) or not value or len(value) > 100:
        raise APIInputError('packages must be a non-empty list of at most 100 names')
    packages = []
    for package in value:
        if not isinstance(package, str) or not PACKAGE_RE.fullmatch(package):
            raise APIInputError('invalid package name')
        packages.append(package)
    return packages
