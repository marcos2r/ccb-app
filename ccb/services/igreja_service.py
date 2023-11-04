from ccb.models.igreja import Igreja
from ccb.services.service import Service
from ccb.repositories.igreja_repository import IgrejaRepository


class IgrejaService(Service):
    def __init__(self):
        super().__init__(repository=IgrejaRepository())

    def get_by_cod(self, cod: str) -> Igreja:
        return self.repository.get_by_cod(cod)
