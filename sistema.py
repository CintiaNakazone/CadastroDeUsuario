usuarios = []

def menu():
    print("\n1 - Cadastrar")
    print("2 - Login")
    print("3 - Listar usuários")
    print("4 - Sair")

def cadastrar():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def login():
    email = input("Email: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            print(f"Bem-vindo, {usuario['nome']}!")
            return
    
    print("Email ou senha incorretos.")

def listar():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    for u in usuarios:
        print(f"Nome: {u['nome']} | Email: {u['email']}")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        listar()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")

import json

def salvar():
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)

def carregar():
    global usuarios
    try:
        with open("usuarios.json", "r") as f:
            usuarios = json.load(f)
    except:
        usuarios = []