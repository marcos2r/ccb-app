"""
Autor: Marcos Ricardo Rodrigues
Data de Alteração: 15/09/2023

Este código cria uma aplicação Flask que se conecta a um banco de dados MongoDB.
Ele obtém documentos da coleção 'igrejas' no banco de dados e fornece esses dados
em formato JSON através de uma rota HTTP '/dados'. A aplicação também lida com erros
e retorna mensagens de erro adequadas em caso de problemas.
"""
import json
from flask import Flask, Response
from flask_cors import CORS
from config import mongodb_name, mongodb_uri
from app.models.mongodb import MongoDB

# Instanciação do objeto MongoDB para conectar ao banco de dados
db = MongoDB()
db.connect()

# Obtém a coleção 'igrejas' do banco de dados
collection = db.get_collection('igrejas')

def obter_dados():
    """
    Obtém os documentos da coleção 'igrejas'.

    Returns:
        list: Uma lista de documentos da coleção 'igrejas'.
    """
    documents = list(collection.find())
    return documents

def criar_app():
    """
    Cria a aplicação Flask.

    Returns:
        Flask: Uma instância da aplicação Flask.
    """
    app = Flask(__name__)
    CORS(app)  # Habilita CORS para o aplicativo

    @app.route("/dados", methods=["GET"])
    def get_data():
        try:
            # Obtém os documentos da coleção 'igrejas' e converte para JSON
            response_data = json.dumps(obter_dados(), default=str)
            return Response(response_data, content_type="application/json", status=200)
        except Exception as e:
            error_message = {"error": str(e)}
            return Response(json.dumps(error_message), content_type="application/json", status=500)

    return app

if __name__ == "__main__":
    app = criar_app()
    app.run()
