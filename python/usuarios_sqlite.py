import sqlite3
import bcrypt


def criptografar_senha(senha):

    senha_bytes = senha.encode("utf-8")

    hash_senha = bcrypt.hashpw(
        senha_bytes,
        bcrypt.gensalt()
    )

    return hash_senha.decode("utf-8")


def conectar_banco():

    conexao = sqlite3.connect("usuarios.db")

    return conexao


def criar_tabela(cursor):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nome TEXT,

        idade INTEGER,

        email TEXT UNIQUE,

        senha TEXT
    )
    """)


def inserir_usuario(cursor,nome,idade,email,senha):

    cursor.execute("""
    INSERT INTO usuarios (
        nome,
        idade,
        email,
        senha
    )
    VALUES (?, ?, ?, ?)
    """, (nome, idade, email, senha))


def listar_usuarios(cursor):

    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    for usuario in usuarios:

        print(usuario)


def buscar_usuario_email(cursor):

    email = input("Digite o email: ")

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE email = ?
    """, (email,))

    usuario = cursor.fetchone()

    if usuario:

        print(usuario)

    else:

        print("Usuario nao encontrado.")


def excluir_usuario(cursor, conexao):

    email = input(
        "Digite o email: "
    )

    cursor.execute("""
    SELECT senha FROM usuarios
    WHERE email = ?
    """, (email,))

    usuario = cursor.fetchone()

    if usuario is None:

        print("Usuario nao encontrado.")
        return

    senha_hash = usuario[0]

    while True:

        senha = input(
            "Digite a senha "
            "(ou 0 para voltar): "
        )

        if senha == "0":

            print("Voltando ao menu...")
            return

        senha_correta = bcrypt.checkpw(
            senha.encode("utf-8"),
            senha_hash.encode("utf-8")
        )

        if senha_correta:

            cursor.execute("""
            DELETE FROM usuarios
            WHERE email = ?
            """, (email,))

            conexao.commit()

            print(
                "Usuario removido com sucesso."
            )

            return

        else:

            print("Senha incorreta.")


def atualizar_usuario(cursor, conexao):

    email = input(
        "Digite o email do usuario: "
    )

    opcao = input(
        "\n1. Nome"
        "\n2. Idade"
        "\n3. Email"
        "\n4. Senha"
        "\nOpcao: "
    )

    if opcao == "1":

        novo_nome = input(
            "Digite o novo nome: "
        )

        cursor.execute("""
        UPDATE usuarios
        SET nome = ?
        WHERE email = ?
        """, (novo_nome, email))


    elif opcao == "2":

        nova_idade = int(input(
            "Digite a nova idade: "
        ))

        cursor.execute("""
        UPDATE usuarios
        SET idade = ?
        WHERE email = ?
        """, (nova_idade, email))


    elif opcao == "3":

        novo_email = input(
            "Digite o novo email: "
        )

        cursor.execute("""
        UPDATE usuarios
        SET email = ?
        WHERE email = ?
        """, (novo_email, email))


    elif opcao == "4":

        nova_senha = input(
            "Digite a nova senha: "
        )

        nova_senha = criptografar_senha(
            nova_senha
        )

        cursor.execute("""
        UPDATE usuarios
        SET senha = ?
        WHERE email = ?
        """, (nova_senha, email))


    else:

        print("Opcao invalida.")
        return

    conexao.commit()

    if cursor.rowcount > 0:

        print(
            "Usuario atualizado com sucesso."
        )

    else:

        print("Usuario nao encontrado.")


def menu():

    print("\n----- MENU -----")

    print("1. Inserir usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Excluir usuario")
    print("5. Atualizar usuario")
    print("0. Sair")


# ---------------- MAIN ----------------

conexao = conectar_banco()

cursor = conexao.cursor()

criar_tabela(cursor)

while True:

    menu()

    opcao = input(
        "Escolha uma opcao: "
    )

    # ---------------- INSERIR ----------------

    if opcao == "1":

        nome = input(
            "Digite o nome: "
        )

        idade = int(input(
            "Digite a idade: "
        ))

        email = input(
            "Digite o email: "
        )

        senha = input(
            "Digite a senha: "
        )

        senha = criptografar_senha(
            senha
        )

        try:

            inserir_usuario(
                cursor,
                nome,
                idade,
                email,
                senha
            )

            conexao.commit()

            print(
                "Usuario inserido com sucesso."
            )

        except sqlite3.IntegrityError:

            print(
                "Email ja cadastrado."
            )

    # ---------------- LISTAR ----------------

    elif opcao == "2":

        listar_usuarios(cursor)

    # ---------------- BUSCAR ----------------

    elif opcao == "3":

        buscar_usuario_email(cursor)

    # ---------------- EXCLUIR ----------------

    elif opcao == "4":

        excluir_usuario(
            cursor,
            conexao
        )

    # ---------------- ATUALIZAR ----------------

    elif opcao == "5":

        atualizar_usuario(
            cursor,
            conexao
        )

    # ---------------- SAIR ----------------

    elif opcao == "0":

        print("Saindo...")

        break

    # ---------------- ERRO ----------------

    else:

        print("Opcao invalida.")

conexao.close()