import os
from neo4j import GraphDatabase
from dotenv import load_dotenv


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Parâmetros de conexão (carregados do .env)
uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

# Função para conectar ao banco de dados Neo4j
def connect_to_neo4j(uri, username, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        session = driver.session()
        return session
    except Exception as e:
        print("Erro ao conectar ao Neo4j:", e)
        return None

# Função para criar uma pessoa no banco de dados
def create_person(session, name, age):
    session.run("CREATE (p:Person {name: $name, age: $age})", name=name, age=age)
    print(f"Pessoa {name} criada com sucesso.")


# Função para listar todas as pessoas no banco de dados
def list_people(session):
    result = session.run("MATCH (p:Person) RETURN p.name AS name, p.age AS age")
    people = result.values()
    if people:
        print("Lista de pessoas:")
        for person in people:
            print(f"Nome: {person[0]}, Idade: {person[1]}")
    else:
        print("Nenhuma pessoa encontrada.")

# Função para buscar uma pessoa específica
def read_person(session, name):
    result = session.run("MATCH (p:Person {name: $name}) RETURN p.name AS name, p.age AS age", name=name)
    person = result.single()
    if person:
        print(f"Pessoa encontrada: Nome: {person['name']}, Idade: {person['age']}")
    else:
        print("Pessoa não encontrada.")

# Função para atualizar a idade de uma pessoa
def update_person_age(session, name, new_age):
    result = session.run("MATCH (p:Person {name: $name}) SET p.age = $new_age RETURN p", name=name, new_age=new_age)
    if result.single():
        print(f"Idade de {name} atualizada para {new_age}.")
    else:
        print("Pessoa não encontrada para atualização.")

# Função para deletar uma pessoa
def delete_person(session, name):
    result = session.run("MATCH (p:Person {name: $name}) DELETE p RETURN COUNT(p) AS count", name=name)
    if result.single()["count"] > 0:
        print(f"Pessoa {name} deletada com sucesso.")
    else:
        print("Pessoa não encontrada para deletar.")

# Função para criar relacionamento de amizade entre duas pessoas
def create_friendship(session, name1, name2):
    result = session.run(
        """
        MATCH (p1:Person {name: $name1}), (p2:Person {name: $name2})
        CREATE (p1)-[:AMIGO]->(p2)
        RETURN p1, p2
        """, name1=name1, name2=name2)
    
    if result.single():
        print(f"Relacionamento de amizade criado entre {name1} e {name2}.")
    else:
        print("Uma ou ambas as pessoas não foram encontradas para criar o relacionamento.")

# Função para deletar todas as pessoas
def delete_all_people(session):
    session.run("MATCH (p:Person) DETACH DELETE p")
    print("Todas as pessoas foram deletadas com sucesso.")

# Função para mostrar o menu e capturar a escolha do usuário
def show_menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar nova pessoa")
    print("2. Listar todas as pessoas")
    print("3. Buscar pessoa")
    print("4. Atualizar idade da pessoa")
    print("5. Deletar pessoa")
    print("6. Criar relacionamento de amizade")
    print("7. Deletar todas as pessoas")
    print("8. Sair")
    return input("Digite o número da opção: ")


# Tentar conectar ao banco de dados
session = connect_to_neo4j(uri, username, password)

# Executar operações de CRUD com interação no terminal
if session:
    print("Conexão com o Neo4j estabelecida com sucesso!")
    
    while True:
        opcao = show_menu()
        
        if opcao == "1":
            name = input("Digite o nome da pessoa: ")
            age = int(input("Digite a idade da pessoa: "))
            create_person(session, name, age)
        
        elif opcao == "2":
            list_people(session)
        
        elif opcao == "3":
            name = input("Digite o nome da pessoa para buscar: ")
            read_person(session, name)
        
        elif opcao == "4":
            name = input("Digite o nome da pessoa para atualizar: ")
            new_age = int(input("Digite a nova idade: "))
            update_person_age(session, name, new_age)
        
        elif opcao == "5":
            name = input("Digite o nome da pessoa para deletar: ")
            delete_person(session, name)
        
        elif opcao == "6":
            name1 = input("Digite o nome da primeira pessoa: ")
            name2 = input("Digite o nome da segunda pessoa: ")
            create_friendship(session, name1, name2)
        
        elif opcao == "7":
            confirm = input("Tem certeza de que deseja deletar todas as pessoas? (s/n): ")
            if confirm.lower() == "s":
                delete_all_people(session)
            else:
                print("Operação cancelada.")
        
        elif opcao == "8":
            print("Encerrando o programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
    
    session.close()  # Fechar a sessão quando terminar
else:
    print("Não foi possível estabelecer conexão com o Neo4j.")
