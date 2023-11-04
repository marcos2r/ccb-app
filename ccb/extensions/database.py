from pymongo import MongoClient

class MongoDB:
    _instance = None
    _client = None
    _uri = None

    @classmethod
    def get_instance(cls, uri=None):
        if cls._instance is None:
            cls._instance = MongoDB()
            if uri:
                cls._uri = uri
                cls._client = MongoClient(cls._uri)
        return cls._instance

    def connect(self, uri):
        if not self._client:
            self._client = MongoClient(uri)

    def close(self):
        if self._client:
            self._client.close()
            self._client = None

    @property
    def db(self):
        if not self._client:
            raise Exception("No active MongoDB connection")
        return self._client["ccb"]

    def get_collection(self, name):
        return self.db[name]


mongodb = MongoDB.get_instance()


def init_app(app):
    mongodb.connect(app.config.MONGO_DATABASE_CONNECTION)
    app.teardown_appcontext(close_mongo_connection)


def close_mongo_connection(exception=None):
    mongodb.close()
