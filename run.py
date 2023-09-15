"""
Autor: Marcos Ricardo Rodrigues
Data de Alteração: 15/09/2023

Este script inicia a aplicação Flask definida no módulo `app`. Ele cria uma instância da aplicação
e tenta iniciar o servidor Flask para escutar em todas as interfaces (0.0.0.0). Em caso de erro
durante a inicialização do servidor, ele trata a exceção e imprime uma mensagem amigável.

É o ponto de entrada para executar sua aplicação Flask.
"""
from app import criar_app  # Importa a função criar_app do seu módulo app

app = criar_app()  # Cria a instância da aplicação Flask

if __name__ == "__main__":
    try:
        # Inicia o servidor Flask, escutando em todas as interfaces (0.0.0.0)
        app.run(host='0.0.0.0')

    except Exception as e:
        # Trata possíveis erros e imprime uma mensagem amigável
        print(f"Erro ao iniciar o servidor: {e}")