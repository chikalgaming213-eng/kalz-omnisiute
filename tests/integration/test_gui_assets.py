from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QML = ROOT / 'kalz/ui/qml/Main.qml'
ASSET = ROOT / 'kalz/ui/assets/kalz-venom.png'


def test_gui_brand_asset_exists_and_is_referenced():
    source = QML.read_text(encoding='utf-8')
    assert ASSET.exists() and ASSET.stat().st_size > 0
    assert 'kalz-venom-48.png' in source
    assert 'icon:' not in source


def test_gui_has_no_known_invalid_application_window_property():
    source = QML.read_text(encoding='utf-8')
    assert 'ApplicationWindow' in source
    assert 'Cannot assign to non-existent property' not in source
