from typing import List, TypeVar
from pydantic import BaseModel

from ccb.repositories.repository import Repository

T = TypeVar('T', bound=BaseModel)


class Service:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_all(self) -> List[T]:
        return self.repository.get_all()

    def get_by_id(self, entity_id) -> T:
        return self.repository.get_by_id(entity_id)

    def insert(self, entity: T) -> T:
        inserted_entity = self.repository.insert(entity)
        return inserted_entity

    def update(self, entity_id, entity: T) -> T:
        updated_entity = self.repository.update(entity_id, entity)
        return updated_entity

    def delete(self, entity_id):
        return self.repository.delete(entity_id)
