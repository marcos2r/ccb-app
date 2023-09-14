from pymongo import MongoClient
from config import mongodb_name, mongodb_uri

class MongoDB:
    def __init__(self) -> None:
        self.__uri = mongodb_uri
        self.__client = None
        self.__db = None


    def connect(self):
        self.__client = MongoClient(self.__uri)
        self.__db = self.__client[mongodb_name]
    
    def get_db(self):
        return self.__db

    def get_collection(self, name):
        collection = self.__db[name]
        documents = []

        for document in collection.find():
            documents.append(document)
        
        return documents