Name: kalz-omnisiute
Version: 0.1.0
Release: 1%{?dist}
Summary: Safe auditable native Linux operations suite
License: MIT
BuildArch: noarch
Requires: python3 >= 3.11

%description
Kalz OmniSuite provides preview-first and consent-gated Linux operations,
observability, distributed processing, gateway routing, and layered defense.

%prep
%setup -q -c -T

%install
mkdir -p %{buildroot}%{_datadir}/kalz-omnisiute
cp -a kalz docs scripts pyproject.toml README.md %{buildroot}%{_datadir}/kalz-omnisiute/

%files
%{_datadir}/kalz-omnisiute

%changelog
* Mon Sep 15 2026 Kalz OmniSuite Maintainers - 0.1.0-1
- Add native Linux operations suite packaging
