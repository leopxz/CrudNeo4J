# CRUD Neo4j com Python
Este é um projeto de CRUD (Create, Read, Update, Delete) para operações em um banco de dados Neo4j utilizando Python. O objetivo é demonstrar como interagir com um banco de dados gráfico de forma prática e eficiente, aplicando operações CRUD.

## Contexto
O projeto foi desenvolvido para facilitar a manipulação de dados em bancos de dados gráficos, especificamente usando o Neo4j, uma tecnologia poderosa para modelagem de relações complexas. O uso do Python como linguagem de programação permite uma interface mais acessível e flexível para realizar operações com o Neo4j.

## Configuração
Para rodar o projeto, é necessário ter:

Python (recomenda-se a versão 3.8 ou superior)

Neo4j (necessário configurar um banco de dados Neo4j local ou remoto)

Bibliotecas do projeto: utilize o Pipfile para instalar as dependências necessárias. Execute o seguinte comando para instalar as dependências do projeto:
```
pipenv install
```
Configuração de Conexão: certifique-se de que o arquivo crud_neo4j.py possui as informações de conexão adequadas para o seu banco de dados Neo4j (URI, usuário e senha).

## Execução
Após configurar o ambiente, você pode executar o script crud_neo4j.py para realizar operações CRUD. Basta rodar o seguinte comando no terminal:
```
pipenv run python crud_neo4j.py
```
O arquivo teste_crud_realizado.text contém exemplos de testes já realizados com operações bem-sucedidas. Ele pode servir como referência para entender o funcionamento das operações e verificar os resultados esperados.

## Estrutura
A estrutura do projeto é composta pelos seguintes arquivos:
<br>
Pipfile e Pipfile.lock: arquivos de configuração para gerenciar as dependências do projeto com pipenv.<br>
crud_neo4j.py: script principal contendo as funções de CRUD para interação com o banco de dados Neo4j.<br>
teste_crud_realizado.text: arquivo de texto contendo exemplos de testes realizados e resultados das operações.<br>
