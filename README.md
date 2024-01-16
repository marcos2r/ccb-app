# ccb-ddos-app

## Descrição

Este projeto é uma API RESTful que fornece informações sobre igrejas da Congregação Cristã do Brasil (CCB).

## Requisitos

* Python 3.8 ou superior
* Pip
* blinker==1.7.0
* bson==0.5.10
* click==8.1.7
* colorama==0.4.6
* dnspython==2.4.2
* Flask==3.0.0
* itsdangerous==2.1.2
* Jinja2==3.1.3
* MarkupSafe==2.1.3
* pymongo==4.6.1
* python-dateutil==2.8.2
* six==1.16.0
* Werkzeug==3.0.1

## Estrutura do Projeto

A estrutura do projeto segue as seguintes convenções:
```
ccb-ddos-app/
│
├── README.md
├── main.py
├── requirements.txt
├── venv/ (ambiente virtual - opcional)
```
Aqui está uma breve descrição de cada um dos principais componentes:

## Como executar

### Clonar o repositório

Para clonar este repositório usando o comando git clone, siga estas etapas:

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde deseja clonar o repositório.
3. Digite o seguinte comando:
```
git clone https://github.com/marcos2r/ccb-ddos-app.git
```

### Iniciar o ambiente virtual do python

#### No Windows
Para criar uma pasta virtual do Python no Windows, abra um prompt de comando e execute o seguinte comando:
```
python -m venv venv
```
Para ativar a pasta virtual, execute o seguinte comando:
```
cd venv
activate
```

### No Linux
Para criar um ambiente virtual do Python no Linux, abra um terminal e execute o seguinte comando:
```
python3 -m venv venv
```
Para ativar a pasta virtual, execute o seguinte comando:
```
source venv/bin/activate
```

### Instalar as dependências
Para instalar as dependências do projeto, execute o seguinte comando:
```
pip install -r requirements.txt
```

### Criar/atualizar um arquivo de dependências
Para criar um arquivo de dependências com o comando pip freeze, siga estas etapas:
1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde deseja criar o arquivo de dependências.
3. Execute o seguinte comando:
```
pip freeze > requirements.txt
```