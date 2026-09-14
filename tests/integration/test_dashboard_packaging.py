from pathlib import Path

from kalz.ui.dashboard import DashboardService

ROOT = Path(__file__).resolve().parents[2]


def test_dashboard_snapshot_is_read_only_and_typed():
    service = DashboardService()
    snapshot = service.snapshot()
    assert snapshot.application == 'Kalz OmniSuite'
    assert snapshot.version
    assert snapshot.gateway_requests == 0
    assert 'logs=' in service.status_text()


def test_packaging_manifests_exist():
    required = [
        ROOT / 'packaging/debian/control',
        ROOT / 'packaging/rpm/kalz-omnisiute.spec',
        ROOT / 'packaging/appimage/AppRun',
        ROOT / 'packaging/appimage/org.kalz.OmniSuite.desktop',
        ROOT / 'packaging/snap/snapcraft.yaml',
    ]
    assert all(path.exists() and path.stat().st_size > 0 for path in required)
