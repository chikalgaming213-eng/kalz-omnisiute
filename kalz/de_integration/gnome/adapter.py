import shutil
from kalz.de_integration.base import BaseDEAdapter, DEStatus


class GNOMEAdapter(BaseDEAdapter):
    name = "gnome"
    def status(self) -> DEStatus:
        caps = tuple(x for x, b in (("shell", shutil.which("gnome-shell")), ("nautilus", shutil.which("nautilus")), ("dconf", shutil.which("dconf"))) if b)
        return DEStatus(self.name, bool(caps), caps)
