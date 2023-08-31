# ccb-ddos-app

O **ccb-ddos-app** é uma aplicação destinada ao cadastro de administrações e igrejas pertencentes a cada administração da Congregação Cristã no Brasil (CCB). Através desta aplicação, você poderá gerenciar informações importantes sobre as igrejas, como dias de culto, endereço e ministério que atende.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `LICENSE`: Este arquivo contém as informações de licença do projeto.
- `README.md`: Este arquivo que você está lendo, fornece informações sobre o projeto.
- `app.py`: O arquivo que contém a implementação da aplicação em linguagem Python.
- `wsgi.py`: Este arquivo executa o serviço da aplicação.
- `JSON/`: Este diretório contém os arquivos JSON com os dados das igrejas.
  - `igrejas.json`: Arquivo JSON que armazena os dados das igrejas.

## Funcionalidades

- Cadastro de administrações e suas igrejas associadas.
- Armazenamento de informações como dias de culto, endereço e ministério que atende para cada igreja.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado o Python e as bibliotecas necessárias. Consulte o arquivo `requirements.txt` para obter a lista completa de dependências.

## Uso

1. Execute o arquivo `app.py` para iniciar a aplicação.
2. Acesse a aplicação através do navegador ou cliente HTTP.
3. Utilize as funcionalidades de cadastro de administrações e igrejas.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, siga estas etapas:

1. Crie um fork deste repositório.
2. Crie uma branch para a sua feature: `git checkout -b minha-feature`
3. Faça commit das suas alterações: `git commit -m 'Adicionar nova feature'`
4. Envie as alterações para o seu fork: `git push origin minha-feature`
5. Abra um pull request neste repositório.

## Passo 1 - Instalação

1. Clone este repositório: `git clone https://github.com/seu-usuario/ccb-ddos-app.git`
2. Acesse o diretório do projeto: `cd ccb-ddos-app`

## Passo 2 - Instalar o virtualenv
Instale o virtualenv para trabalhar com ambientes virtuais no python utilizando o comando:
```
pip install virtualenv
```
Caso dê problema com a versão do pip atual, atualize o pip utilizando:
```
python -m pip install --upgrade pip
```

## Passo 3 - Ative o virtualenv
Para ativar o ambiente virtual rode:
```
virtualenv venv
```

## Passo 4 - (Depende do seu sistema operacional)
### Windows
```
.\venv\Scripts\activate
```

### Linux
```
source venv/bin/activate
```
Para saber se deu certo a ativação, basta ver se fica ```(venv)``` aparecendo antes do caminho no terminal

## Passo 5 - Instalar as dependências
Com o ambiente virtual ativado, toda instalação de biblioteca externa fica somente no ambiente virtual, ao invés de sujar sua instalação do python na máquina local

Com o ambiente virtual instalado, execute o comando abaixo para instalar as dependências
```
pip install -r requirements.txt
```

## Observação
Para atualizar o `requirements.txt` com novas dependências que adicionar, basta executar
```
pip freeze > requirements.txt
```

## Licença

Este projeto está sob a licença GNU General Public License v3.0. Consulte o arquivo `LICENSE` para obter mais detalhes.

## Contato

Para mais informações, entre em contato com Marcos Ricardo Rodrigues via bcc.marcos@gmail.com ou @marcos2_r(https://www.instagram.com/marcos2_r/).
