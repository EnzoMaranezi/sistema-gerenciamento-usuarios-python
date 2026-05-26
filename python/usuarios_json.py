import json
import os

def validar_idade(idade, nome):
   
    while True:

        try:
            idade = int(idade)

            if idade < 0 or idade > 120:
                idade = input(f"Idade invalida do {nome}, digite novamente: ")
                continue

            return idade

        except ValueError:
            idade = input(f"Idade invalida para {nome}, digite novamente usando numeros: ")


def validar_senha(senha, nome):

    while len(senha) < 5:

        senha = input(
            f"Senha do usuario {nome} está inválida, digite a nova senha com no minimo 5 caracteres: "
        )

    return senha

def validar_email(email, usuarios):

    while True:

        if "@" not in email or "." not in email:

            email = input(f" {email} é invalido, digite novamente: ")

            continue

        email_existe = False

        for usuario in usuarios:

            if usuario["email"] == email:

                email_existe = True

                print("Email já cadastrado")

                email = input("Digite outro email: ")

                break

        if not email_existe:
            return email
        
def carregar_usuarios():

    caminho_arquivo = os.path.join(
    os.path.dirname(__file__),
    "entrada_saida",
    "json",
    "usuarios.json"
)

    with open(
        caminho_arquivo,
        "r",
        encoding="utf-8"
    ) as arquivo:

        usuarios = json.load(arquivo)

    return usuarios



def salvar_usuarios(usuarios):

    caminho_arquivo = os.path.join(
    os.path.dirname(__file__),
    "entrada_saida",
    "json",
    "usuarios_saida.json"
)

    with open(
        caminho_arquivo,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            usuarios,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

def cadastrar_usuario(usuarios):
    novo_nome = input("Digite o nome do usuario: ")
    
    nova_idade = input("Digite a idade do usuario: ")
    nova_idade = validar_idade(nova_idade, novo_nome)

    novo_email = input("Digite o email do usuario: ")
    novo_email = validar_email(novo_email,usuarios)

    nova_senha = input("Digite a senha do usuario: ")
    nova_senha = validar_senha(nova_senha, novo_nome)

    usuario = {
            "nome": novo_nome,
            "idade": nova_idade,
            "email": novo_email,
            "senha": nova_senha
        }

    usuarios.append(usuario)
    # return usuarios nao é obrigatorio porque o append ja retorna a lista 

def listar_usuarios(usuarios):
    print("\n")
    for indice, usuario in enumerate(usuarios):

     print(
        f"{indice + 1}. "
        f"{usuario['nome']} | "
        f"{usuario['idade']} | "
        f"{usuario['email']} | "
        f"{usuario['senha']}"
    )

def buscar_usuario_email(usuarios):
    
   usuario_encontrado = False
   email = input("Digite o email do usuario: ")
   for usuario in usuarios:

    if usuario["email"] == email:
        usuario_encontrado = True
        print(
         "\nOs dados do usuario sao:\n"
        f"{usuario['nome']} | "
        f"{usuario['idade']} | "
        f"{usuario['email']} | "
        f"{usuario['senha']}"
    ) 
    
   if usuario_encontrado == False:
     print("Usuario nao encontrado.")

def excluir_usuario(usuarios):
    email = input("Digite o email do usuario a ser excluido: ")

    for usuario in usuarios:
        if usuario["email"] == email:
            usuarios.remove(usuario)
            print("Usuario excluido com sucesso.")
            return

    print("Usuario nao encontrado.")

def atualizar_usuario(usuarios):

    email = input("Insira o email do usuario: ")

    for usuario in usuarios:

        if usuario["email"] == email:

            ans = input(
                "\nDigite qual campo do usuario deseja atualizar:"
                "\n1. Nome"
                "\n2. Idade"
                "\n3. Email"
                "\n4. Senha"
                "\nOpcao: "
            )

            if ans == "1":

                novo_nome = input(
                    "Digite o novo nome do usuario: "
                )

                usuario["nome"] = novo_nome

            elif ans == "2":

                nova_idade = input(
                    "Digite a nova idade do usuario: "
                )

                nova_idade = validar_idade(
                    nova_idade,
                    usuario["nome"]
                )

                usuario["idade"] = nova_idade

            elif ans == "3":

                novo_email = input(
                    "Digite o novo email do usuario: "
                )

                novo_email = validar_email(
                    novo_email,
                    usuarios
                )

                usuario["email"] = novo_email

            elif ans == "4":

                nova_senha = input(
                    "Digite a nova senha do usuario: "
                )

                nova_senha = validar_senha(
                    nova_senha,
                    usuario["nome"]
                )

                usuario["senha"] = nova_senha

            else:
                print("Opcao invalida.")

            print("Usuario atualizado com sucesso.")

            return

    print("Usuario nao encontrado.")


def menu():
    print("\n----- MENU -----")
    print("1. Listar todos os usuarios")
    print("2. Cadastrar novo usuario")
    print("3. Buscar usuario")
    print("4. Remover usuario")
    print("5. Salvar usuarios")
    print("6. Atualizar usuario")
    print("0. Sair")

usuarios = carregar_usuarios()

while True:
    menu()

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        listar_usuarios(usuarios)

    elif opcao == "2":
        cadastrar_usuario(usuarios)

    elif opcao == "3":
        buscar_usuario_email(usuarios)

    elif opcao == "4":
        excluir_usuario(usuarios)

    elif opcao == "5":
        salvar_usuarios(usuarios)
        print("Usuarios salvos com sucesso.")

    elif opcao == "6":
        atualizar_usuario(usuarios)

    elif opcao == "0":
        salvar_usuarios(usuarios)
        print("Saindo...")
        break

    else:
        print("Opcao invalida.")



