"""
MongoDB Manager - Gerenciador de Conexão MongoDB

Este módulo contém a classe MongoDBManager, que oferece métodos para conectar e operar com um banco de dados MongoDB.

Autor: Marcos Ricardo Rodrigues
Data de Criação: 09 de setembro de 2023

Licença: GNU General Public License v3.0

Para usar este módulo, forneça as informações de conexão e utilize os métodos da classe MongoDBManager para interagir com o MongoDB.
"""

# Importe a biblioteca pymongo para interagir com o MongoDB
import pymongo


class MongoDBManager:
    def __init__(self, host, port, username, password, database):
        """
        Inicializa a classe com as informações de conexão ao MongoDB.

        Args:
            host (str): O endereço do servidor MongoDB.
            port (int): A porta do servidor MongoDB.
            username (str): O nome de usuário para autenticação (pode ser None se não houver autenticação).
            password (str): A senha do usuário para autenticação (pode ser None se não houver autenticação).
            database (str): O nome do banco de dados MongoDB a ser utilizado.
        """
        # Configurar as informações de conexão
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.client = None  # Objeto de cliente MongoDB

    def connect(self):
        """
        Estabelece a conexão com o servidor MongoDB.
        """
        try:
            # Crie uma conexão com o servidor MongoDB
            self.client = pymongo.MongoClient(self.host, self.port)

            # Autentique-se se as credenciais de usuário foram fornecidas
            if self.username and self.password:
                self.client[self.database].authenticate(
                    self.username, self.password)

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

    def get_collection(self, collection_name):
        """
        Obtém uma referência a uma coleção no banco de dados.

        Args:
            collection_name (str): O nome da coleção.

        Returns:
            pymongo.collection.Collection: Uma referência à coleção.
        """
        if self.client:
            return self.client[self.database][collection_name]
        else:
            print("Erro: Conexão não estabelecida.")
            return None

    def insert_document(self, collection_name, document):
        """
        Insere um documento em uma coleção.

        Args:
            collection_name (str): O nome da coleção.
            document (dict): O documento a ser inserido.

        Returns:
            pymongo.results.InsertOneResult: O resultado da operação de inserção.
        """
        collection = self.get_collection(collection_name)
        if collection:
            try:
                result = collection.insert_one(document)
                return result
            except Exception as e:
                print(f"Erro ao inserir documento: {e}")
        return None

    def find_documents(self, collection_name, query):
        """
        Encontra documentos em uma coleção com base em uma consulta.

        Args:
            collection_name (str): O nome da coleção.
            query (dict): A consulta a ser executada.

        Returns:
            list: Uma lista de documentos que correspondem à consulta.
        """
        collection = self.get_collection(collection_name)
        if collection:
            try:
                cursor = collection.find(query)
                return list(cursor)
            except Exception as e:
                print(f"Erro ao buscar documentos: {e}")
        return []

    def update_document(self, collection_name, query, update):
        """
        Atualiza documentos em uma coleção com base em uma consulta.

        Args:
            collection_name (str): O nome da coleção.
            query (dict): A consulta para encontrar os documentos a serem atualizados.
            update (dict): As atualizações a serem aplicadas aos documentos correspondentes.

        Returns:
            pymongo.results.UpdateResult: O resultado da operação de atualização.
        """
        collection = self.get_collection(collection_name)
        if collection:
            try:
                result = collection.update_many(query, {"$set": update})
                return result
            except Exception as e:
                print(f"Erro ao atualizar documentos: {e}")
        return None

    def delete_document(self, collection_name, query):
        """
        Exclui documentos de uma coleção com base em uma consulta.

        Args:
            collection_name (str): O nome da coleção.
            query (dict): A consulta para encontrar os documentos a serem excluídos.

        Returns:
            pymongo.results.DeleteResult: O resultado da operação de exclusão.
        """
        collection = self.get_collection(collection_name)
        if collection:
            try:
                result = collection.delete_many(query)
                return result
            except Exception as e:
                print(f"Erro ao excluir documentos: {e}")
        return None

'''
# Exemplo de uso da classe MongoDBManager
if __name__ == "__main__":
    # Parâmetros de conexão ao MongoDB
    host = "localhost"
    port = 27017
    # Coloque seu nome de usuário (ou None se não houver autenticação)
    username = "seu_usuario"
    # Coloque sua senha (ou None se não houver autenticação)
    password = "sua_senha"
    database = "seu_banco_de_dados"  # Coloque o nome do seu banco de dados

    # Crie uma instância da classe MongoDBManager
    manager = MongoDBManager(host, port, username, password, database)

    # Conecte-se ao MongoDB
    manager.connect()

    # Exemplo: Inserir um documento em uma coleção
    documento = {"nome": "João", "idade": 30}
    resultado = manager.insert_document("pessoas", documento)
    print(f"Documento inserido com ID: {resultado.inserted_id}")

    # Exemplo: Consultar documentos em uma coleção
    consulta = {"nome": "João"}
    documentos_encontrados = manager.find_documents("pessoas", consulta)
    print("Documentos encontrados:")
    for doc in documentos_encontrados:
        print(doc)

    # Desconecte-se do MongoDB
    manager.disconnect()
    '''
