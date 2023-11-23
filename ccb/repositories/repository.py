from typing import TypeVar, Type, List
from pydantic import BaseModel

from ccb.extensions.database import mongodb

T = TypeVar("T", bound=BaseModel)


class Repository:
    def __init__(self, collection_name: str, model: Type[T]):
        self.collection = mongodb.get_collection(collection_name)
        self.model = model

    def get_all(self) -> List[T]:
        results = list(self.collection.find())
        return results

    def get_by_id(self, entity_id: str) -> T:
        result = self.collection.find_one({"_id": entity_id})
        return self.model(**result) if result else None

    def insert(self, entity: T):
        return self.collection.insert_one(entity.model_jump_json())

    def update(self, entity_id, entity: T):
        return self.collection.update_one({"_id": entity_id}, {"$set": entity.model_jump_json()})

    def delete(self, entity_id):
        return self.collection.delete_one({"_id": entity_id})
