from typing import Type

from ccb.models.igreja import Igreja

from ccb.repositories.repository import Repository


class IgrejaRepository(Repository):
    def __init__(self):
        super().__init__(collection_name="igrejas", model=Type[Igreja])

    def get_by_cod(self, cod: str) -> Igreja:
        result = self.collection.find_one({"cod": cod})
        return self.model(**result) if result else None
