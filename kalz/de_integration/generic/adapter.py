from kalz.de_integration.base import BaseDEAdapter, DEStatus


class GenericAdapter(BaseDEAdapter):
    name = "generic"

    def status(self) -> DEStatus:
        return DEStatus(self.name, True, ("desktop-entry", "notifications"))
