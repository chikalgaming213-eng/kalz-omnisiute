import shutil
from kalz.de_integration.base import BaseDEAdapter, DEStatus


class XFCEAdapter(BaseDEAdapter):
    name = "xfce"
    def status(self) -> DEStatus:
        caps = tuple(x for x, b in (("panel", shutil.which("xfce4-panel")), ("thunar", shutil.which("thunar")), ("xfconf", shutil.which("xfconf-query"))) if b)
        return DEStatus(self.name, bool(caps), caps)
