from __future__ import annotations

from pathlib import Path


def run_gui() -> int:
    try:
        from PySide6.QtCore import QUrl
        from PySide6.QtQml import QQmlApplicationEngine
        from PySide6.QtWidgets import QApplication
    except ImportError:
        print('PySide6 is not installed; install kalz-omnisiute[ui]')
        return 2
    app = QApplication([])
    engine = QQmlApplicationEngine()
    qml = Path(__file__).parent / 'ui' / 'qml' / 'Main.qml'
    engine.load(QUrl.fromLocalFile(str(qml)))
    if not engine.rootObjects(): return 1
    return app.exec()
