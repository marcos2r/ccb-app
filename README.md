# ccb-ddos-app

O **ccb-ddos-app** é uma aplicação destinada ao cadastro de administrações e igrejas pertencentes a cada administração da Congregação Cristã no Brasil (CCB). Através desta aplicação, você poderá gerenciar informações importantes sobre as igrejas, como dias de culto, endereço e ministério que atende.

## Funcionalidades

- Cadastro de administrações e suas igrejas associadas.
- Armazenamento de informações como dias de culto, endereço e ministério que atende para cada igreja.

## Estrutura do Projeto

A estrutura do projeto segue as seguintes convenções:
```
meu_projeto_flask/
│
├── app/
│   ├── __init__.py
│   ├── modelos.py
│   ├── rotas.py
│   ├── views.py
│   ├── static/
│   └── templates/
│
├── config.py
├── requirements.txt
├── run.py
├── README.md
├── venv/ (ambiente virtual - opcional)
└── outros_recursos/
```
Aqui está uma breve descrição de cada um dos principais componentes:

- **app/**: Este diretório contém o código principal da aplicação Flask.

    - `__init__.py`: Inicializa a aplicação Flask e configura extensões.
    - `modelos.py`: Define os modelos de dados (se estiver usando um ORM como o SQLAlchemy).
    - `rotas.py`: Define as rotas da aplicação e as funções de visualização.
    - `views.py`: Define as views da aplicação (se estiver usando Blueprints).
    - `static/`: Contém arquivos estáticos, como CSS, JavaScript e imagens.
    - `templates/`: Armazena modelos HTML usados para renderizar páginas da web.

- **config.py**: Este arquivo contém configurações da aplicação, como chaves secretas, configurações de banco de dados, etc.

- **requirements.txt**: Lista as dependências da aplicação Flask, que podem ser instaladas usando o `pip`.

- **run.py**: É o ponto de entrada da aplicação que executa o servidor de desenvolvimento Flask.

- **README.md**: Este arquivo de documentação que você está lendo agora, fornece informações sobre o projeto, configuração e instruções de uso.

- **venv/** (opcional): Este é um ambiente virtual que isola as dependências do projeto para evitar conflitos com outras aplicações Python no sistema.

- **outros_recursos/**: Este diretório pode conter quaisquer outros recursos relacionados ao projeto, como scripts, arquivos de configuração adicionais ou qualquer coisa que seja específica do seu projeto.

## `run.py` - Script de Inicialização da Aplicação Flask

Este script é o ponto de entrada para a execução da aplicação Flask definida no módulo `app`. Ele realiza as seguintes ações:

1. Importa a função `criar_app` do módulo `app`, responsável por criar uma instância da aplicação Flask.

2. Cria uma instância da aplicação Flask utilizando a função `criar_app()`.

3. Tenta iniciar o servidor Flask para escutar em todas as interfaces (0.0.0.0).

4. Em caso de erro durante a inicialização do servidor, trata a exceção e imprime uma mensagem amigável.

**Utilização:**

- Execute este script para iniciar a sua aplicação Flask.

**Exemplo:**

```
python run.py
```

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado o Python e as bibliotecas necessárias. Consulte o arquivo `requirements.txt` para obter a lista completa de dependências.

## Uso

1. Execute o arquivo `run.py` para iniciar a aplicação.
2. Acesse a aplicação através do navegador ou cliente HTTP.
3. Utilize as funcionalidades de cadastro de administrações e igrejas.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, siga estas etapas:

1. Crie um fork deste repositório.
2. Crie uma branch para a sua feature: `git checkout -b minha-feature`
3. Faça commit das suas alterações: `git commit -m 'Adicionar nova feature'`
4. Envie as alterações para o seu fork: `git push origin minha-feature`
5. Abra um pull request neste repositório.

## Como Usar

### Passo 1 - Instalação

1. Clone este repositório: 
```
git clone https://github.com/seu-usuario/ccb-ddos-app.git
```
2. Acesse o diretório do projeto: 
```
cd ccb-ddos-app
```

### Passo 2 - Instalar o virtualenv
Instale o virtualenv para trabalhar com ambientes virtuais no python utilizando o comando:
```
python3 -m venv venv
```
Caso dê problema com a versão do pip atual, atualize o pip utilizando:
```
python -m pip install --upgrade pip
```

### Passo 3 - Ative o virtualenv
Para ativar sua pasta virtual, execute o seguinte comando:

#### Windows
```
.\venv\Scripts\activate
```

#### Linux
```
source venv/bin/activate
```
Sua pasta virtual está agora ativada. Você pode verificar se ela está ativada executando o seguinte comando:
```
which python
```

### Passo 5 - Instalar as dependências
Com o ambiente virtual ativado, toda instalação de biblioteca externa fica somente no ambiente virtual, ao invés de sujar sua instalação do python na máquina local

Com o ambiente virtual instalado, execute o comando abaixo para instalar as dependências
```
pip install -r requirements.txt
```
### Passo 6 - Criar o arquivo .env
1. Crie o arquivo .env: No diretório raiz do seu projeto, crie um arquivo chamado .env.
2. Defina Variáveis de Ambiente: Dentro do arquivo .env, como no exemplo abaixo:
```
MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_USERNAME=seu_usuario
MONGODB_PASSWORD=sua_senha
MONGODB_DATABASE=seu_banco_de_dados
```
Observação: Lembre-se de substituir os valores das variáveis conforme sua configuração.

### Observação
Para atualizar o `requirements.txt` com novas dependências que adicionar, basta executar
```
pip freeze > requirements.txt
```

## Licença

Este projeto está sob a licença GNU General Public License v3.0. Consulte o arquivo `LICENSE` para obter mais detalhes.

## Contato

Para mais informações, entre em contato com:

Marcos Ricardo Rodrigues (bcc.marcos@gmail.com)

Gabriel Moya (gabrielmoya123@gmail.com)