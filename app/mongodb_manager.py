import pymongo
from pymongo.server_api import ServerApi

class MongoDBManager:
    def __init__(self, uri, server_api_version='1'):
        """
        Inicializa a classe com a string de conexão ao MongoDB Atlas.

        Args:
            uri (str): A string de conexão ao MongoDB Atlas.
            server_api_version (str): A versão da API do servidor (padrão é '1' para a API estável).
        """
        self.uri = uri
        self.server_api_version = server_api_version
        self.client = None  # Objeto de cliente MongoDB

    def connect(self):
        """
        Estabelece a conexão com o servidor MongoDB.
        """
        try:
            # Crie uma conexão com o servidor MongoDB Atlas
            self.client = pymongo.MongoClient(self.uri, server_api=ServerApi(self.server_api_version))
            print("Conexão bem-sucedida ao MongoDB")

        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")

    def disconnect(self):
        """
        Fecha a conexão com o servidor MongoDB.
        """
        if self.client:
            self.client.close()
            print("Conexão com o MongoDB encerrada")

    def get_collection(self, database_name, collection_name):
        """
        Obtém uma referência a uma coleção no banco de dados.

        Args:
            database_name (str): O nome do banco de dados.
            collection_name (str): O nome da coleção.

        Returns:
            pymongo.collection.Collection: Uma referência à coleção.
        """
        if self.client:
            return self.client[database_name][collection_name]
        else:
            print("Erro: Conexão não estabelecida.")
            return None

    def insert_document(self, database_name, collection_name, document):
        """
        Insere um documento em uma coleção.

        Args:
            database_name (str): O nome do banco de dados.
            collection_name (str): O nome da coleção.
            document (dict): O documento a ser inserido.

        Returns:
            pymongo.results.InsertOneResult: O resultado da operação de inserção.
        """
        collection = self.get_collection(database_name, collection_name)
        if collection:
            try:
                result = collection.insert_one(document)
                return result
            except Exception as e:
                print(f"Erro ao inserir documento: {e}")
        return None

    def find_documents(self, database_name, collection_name, query):
        """
        Encontra documentos em uma coleção com base em uma consulta.

        Args:
            database_name (str): O nome do banco de dados.
            collection_name (str): O nome da coleção.
            query (dict): A consulta a ser executada.

        Returns:
            list: Uma lista de documentos que correspondem à consulta.
        """
        collection = self.get_collection(database_name, collection_name)
        if collection:
            try:
                cursor = collection.find(query)
                return list(cursor)
            except Exception as e:
                print(f"Erro ao buscar documentos: {e}")
        return []

    def update_document(self, database_name, collection_name, query, update):
        """
        Atualiza documentos em uma coleção com base em uma consulta.

        Args:
            database_name (str): O nome do banco de dados.
            collection_name (str): O nome da coleção.
            query (dict): A consulta para encontrar os documentos a serem atualizados.
            update (dict): As atualizações a serem aplicadas aos documentos correspondentes.

        Returns:
            pymongo.results.UpdateResult: O resultado da operação de atualização.
        """
        collection = self.get_collection(database_name, collection_name)
        if collection:
            try:
                result = collection.update_many(query, {"$set": update})
                return result
            except Exception as e:
                print(f"Erro ao atualizar documentos: {e}")
        return None

    def delete_document(self, database_name, collection_name, query):
        """
        Exclui documentos de uma coleção com base em uma consulta.

        Args:
            database_name (str): O nome do banco de dados.
            collection_name (str): O nome da coleção.
            query (dict): A consulta para encontrar os documentos a serem excluídos.

        Returns:
            pymongo.results.DeleteResult: O resultado da operação de exclusão.
        """
        collection = self.get_collection(database_name, collection_name)
        if collection:
            try:
                result = collection.delete_many(query)
                return result
            except Exception as e:
                print(f"Erro ao excluir documentos: {e}")
        return None

