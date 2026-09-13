import shutil
from kalz.de_integration.base import BaseDEAdapter, DEStatus


class KDEAdapter(BaseDEAdapter):
    name = "kde"
    def status(self) -> DEStatus:
        caps = tuple(x for x, b in (("plasma", shutil.which("plasmashell")), ("krunner", shutil.which("krunner")), ("kwallet", shutil.which("kwallet-query"))) if b)
        return DEStatus(self.name, bool(caps), caps)
