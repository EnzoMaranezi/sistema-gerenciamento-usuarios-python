# Sistema de Gerenciamento de Usuários em Python

Projeto desenvolvido em Python com foco em aprendizado de backend, persistência de dados e organização de projetos.

O sistema permite realizar operações completas de CRUD (Create, Read, Update e Delete) utilizando diferentes formas de armazenamento:

- Arquivos TXT
- Arquivos JSON
- Banco de dados SQLite

Além disso, o projeto utiliza criptografia de senhas com bcrypt para maior segurança.

---

# Funcionalidades

- Cadastro de usuários
- Listagem de usuários
- Busca por email
- Atualização de dados
- Exclusão de usuários
- Persistência em TXT
- Persistência em JSON
- Persistência em SQLite
- Criptografia de senhas
- Validação de email
- Estrutura modularizada

---

# Tecnologias Utilizadas

- Python 3
- SQLite3
- JSON
- bcrypt

---

# Estrutura do Projeto

```text
python/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── usuarios_txt.py
├── usuarios_json.py
├── usuarios_sqlite.py
│
├── entrada_saida/
│   ├── txt/
│   └── json/
│
├── database/
│   └── usuarios.db
│
└── venv/
```

---

# Instalação

## Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

---

## Entre na pasta do projeto

```bash
cd python
```

---

## Crie o ambiente virtual

### Linux

```bash
python3 -m venv venv
```

### Windows

```bash
python -m venv venv
```

---

## Ative o ambiente virtual

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Instale as dependências

```bash
pip install -r requirements.txt
```

---

# Executando o Projeto

```bash
python nome_arquivo.py
```

Exemplos:

```bash
python usuarios_txt.py
python usuarios_json.py
python usuarios_sqlite.py
```

---

# Segurança

As senhas dos usuários são armazenadas utilizando hash com bcrypt, evitando o armazenamento de senhas em texto puro.

---

# Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de praticar:

- lógica de programação
- manipulação de arquivos
- persistência de dados
- SQL
- organização de projetos Python
- autenticação básica
- boas práticas iniciais de backend

---

# Melhorias Futuras

- Login de usuários
- API com FastAPI
- Interface gráfica
- Integração frontend
- Docker
- Deploy

---

# Autor

Enzo Maranezi