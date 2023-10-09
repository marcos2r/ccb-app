"""
Resumo:
Este código define um Blueprint no Flask para criar rotas da API relacionadas à coleção 'igrejas'
em um banco de dados MongoDB. Ele conecta ao banco de dados, obtém os documentos da coleção 'igrejas'
e fornece esses dados em formato JSON através da rota '/igrejas'. Em caso de exceção, ele retorna
uma mensagem de erro com um status HTTP 500.
"""

from flask import Blueprint, Response, json
from app.models.mongodb import MongoDB  # Importe o objeto MongoDB se necessário

# Crie um Blueprint para definir suas rotas
bp = Blueprint("routes", __name__)

# Conecte ao banco de dados e obtenha a coleção 'igrejas' se necessário
db = MongoDB()  # Instância do MongoDB
db.connect()  # Conecta ao banco de dados MongoDB
collection = db.get_collection('igrejas')  # Obtém a coleção 'igrejas' do banco de dados

@bp.route("/igrejas", methods=["GET"])
def get_data():
    try:
        # Obtém os documentos da coleção 'igrejas' e converte para JSON
        documents = list(collection.find())  # Recupera os documentos da coleção 'igrejas'
        response_data = json.dumps(documents, default=str)  # Converte os documentos em JSON
        return Response(response_data, content_type="application/json", status=200)  # Resposta HTTP com os dados JSON
    except Exception as e:
        error_message = {"error": str(e)}  # Mensagem de erro em caso de exceção
        return Response(json.dumps(error_message), content_type="application/json", status=500)  # Resposta de erro HTTP com a mensagem de erro