import pymongo
from pymongo.server_api import ServerApi

class MongoDBManager:
    def __init__(self, uri, dbname, server_api_version='1'):
        """
        Inicializa a classe com a string de conexão ao MongoDB Atlas.

        Args:
            uri (str): A string de conexão ao MongoDB Atlas.
            server_api_version (str): A versão da API do servidor (padrão é '1' para a API estável).
        """
        self.uri = uri
        self.server_api_version = server_api_version
        self.dbname = dbname
        self.client = None  # Objeto de cliente MongoDB
        self.mydb = None


    def connect(self):
        """
        Estabelece a conexão com o servidor MongoDB.
        """
        try:
            # Crie uma conexão com o servidor MongoDB Atlas
            self.client = pymongo.MongoClient(self.uri, server_api=ServerApi(self.server_api_version))
            self.mydb = self.client[self.dbname]
            return True

        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")
        
        return False

    def get_collection(self, name):
        collection = self.mydb[name]
        documents = []

        for document in collection.find():
            documents.append(document)
        
        return documents