# CCB Dourados app

# Passo 1 - Instalar o virtualenv
Instale o virtualenv para trabalhar com ambientes virtuais no python utilizando o comando:
```
pip install virtualenv
```
Caso dê problema com a versão do pip atual, atualize o pip utilizando:
```
python -m pip install --upgrade pip
```

# Passo 2 - Ative o virtualenv
Para ativar o ambiente virtual rode:
```
virtualenv venv
```

# Passo 3 - (Depende do seu sistema operacional)
## Windows
```
.\venv\Scripts\activate
```

## Linux
```
source venv/bin/activate
```
Para saber se deu certo a ativação, basta ver se fica ```(venv)``` aparecendo antes do caminho no terminal

# Passo 4 - Instalar as dependências
Com o ambiente virtual ativado, toda instalação de biblioteca externa fica somente no ambiente virtual, ao invés de sujar sua instalação do python na máquina local

Com o ambiente virtual instalado, execute o comando abaixo para instalar as dependências
```
pip install -r requirements.txt
```

# Observação
Para atualizar o `requirements.txt` com novas dependências que adicionar, basta executar
```
pip freeze > requirements.txt
```
