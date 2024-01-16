# ccb-ddos-app

## Descrição

Este projeto é uma API RESTful que fornece informações sobre igrejas da Confederação Cristã do Brasil (CCB).

## Requisitos

* Python 3.8 ou superior
* Pip
* Flask
* PyMongo

## Como executar

### Clonar o repositório

Para clonar este repositório usando o comando git clone, siga estas etapas:

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde deseja clonar o repositório.
3. Digite o seguinte comando:
'''
git clone https://github.com/marcos2r/ccb-ddos-app.git
'''

### Iniciar o ambiente virtual do python

#### No Windows
Para criar uma pasta virtual do Python no Windows, abra um prompt de comando e execute o seguinte comando:
'''
python -m venv venv
'''
Para ativar a pasta virtual, execute o seguinte comando:
'''
cd venv
activate
'''

### No Linux
Para criar um ambiente virtual do Python no Linux, abra um terminal e execute o seguinte comando:
'''
python3 -m venv venv
'''
Para ativar a pasta virtual, execute o seguinte comando:
'''
source venv/bin/activate
'''

### Instalar as dependências
Para instalar as dependências do projeto, execute o seguinte comando:
'''
pip install -r requirements.txt
'''

### Criar/atualizar um arquivo de dependências
Para criar um arquivo de dependências com o comando pip freeze, siga estas etapas:
1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde deseja criar o arquivo de dependências.
3. Execute o seguinte comando:
'''
pip freeze > requirements.txt
'''