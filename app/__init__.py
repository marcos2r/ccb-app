'''
Em resumo, esse código é responsável por configurar uma aplicação Flask para lidar com rotas e habilitar o suporte a CORS,
tornando-a pronta para ser executada e para responder a solicitações HTTP. 
As rotas e a lógica de manipulação de solicitações provavelmente estão definidas no Blueprint app.routes.
'''

# Importa a classe Flask do framework Flask e o módulo CORS para lidar com CORS (Cross-Origin Resource Sharing).
from flask import Flask
from flask_cors import CORS

# Importa o Blueprint (rotas) definido no módulo app.routes.
from app.routes import bp

# Define uma função para criar a aplicação Flask.
def criar_app():
    # Cria uma instância da aplicação Flask com o nome do módulo atual (__name__).
    app = Flask(__name__)
    
    # Habilita o CORS para permitir solicitações de origens diferentes.
    CORS(app)
    
    # Registra o Blueprint das rotas na aplicação, incluindo as rotas definidas nele.
    app.register_blueprint(bp)

    # Retorna a instância da aplicação Flask criada.
    return app