from app import criar_app  # Importa a função criar_app do seu módulo app

app = criar_app()  # Cria a instância da aplicação Flask

if __name__ == "__main__":
    try:
        # Inicia o servidor Flask, escutando em todas as interfaces (0.0.0.0)
        app.run(host='0.0.0.0')

    except Exception as e:
        # Trata possíveis erros e imprime uma mensagem amigável
        print(f"Erro ao iniciar o servidor: {e}")