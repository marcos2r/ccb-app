"""
Autor: Marcos Ricardo Rodrigues
Data de Alteração: 15/09/2023

Este código define uma classe `MongoDB` que facilita a conexão com um banco de dados MongoDB.
Ele inicializa a classe com informações da URI e configurações do banco de dados. A classe possui
métodos para conectar ao MongoDB, obter coleções e desconectar. Também trata exceções e imprime
mensagens de erro apropriadas em caso de problemas na conexão ou nas operações.

É um utilitário reutilizável para interagir com o MongoDB em outras partes do projeto.
"""
from pymongo import MongoClient
from config import mongodb_name, mongodb_uri

class MongoDB:
    def __init__(self) -> None:
        # Inicializa a classe MongoDB com as informações da URI e configurações do banco de dados
        self.__uri = mongodb_uri
        self.__client = None
        self.__db = None

    def connect(self):
        try:
            # Tenta estabelecer a conexão com o MongoDB usando a URI
            self.__client = MongoClient(self.__uri)
            self.__db = self.__client[mongodb_name]
            print("Conexão bem-sucedida ao MongoDB")
        except Exception as e:
            # Em caso de erro na conexão, imprime a mensagem de erro
            print(f"Erro ao conectar ao MongoDB: {e}")

    def get_collection(self, name):
        try:
            # Obtém uma coleção do banco de dados
            collection = self.__db[name]

            return collection
        except Exception as e:
            # Em caso de erro na obtenção da coleção ou busca de documentos, imprime a mensagem de erro
            print(f"Erro ao obter documentos da coleção {name}: {e}")
            return []

    def disconnect(self):
        try:
            if self.__client:
                self.__client.close()
                print("Conexão com o MongoDB encerrada")
        except Exception as e:
            print(f"Erro ao encerrar a conexão com o MongoDB: {e}")