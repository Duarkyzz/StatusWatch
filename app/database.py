import os
import hashlib
import psycopg2

from dotenv import load_dotenv


# Carrega as variáveis que estão no arquivo .env
load_dotenv()

# Pega a URL do PostgreSQL que colocamos no .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria a conexão com o PostgreSQL do Supabase
conection = psycopg2.connect(DATABASE_URL)

# Cursor usado para executar comandos SQL
cursor = conection.cursor()


def cadastrar_usuario(email, senha):

    if not email or not senha:
        return "Preencha os dados primeiro!"

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    try:
        cursor.execute(
            '''INSERT INTO usuarios (email, senha_hash)
               VALUES (%s, %s)''',
            (email, senha_hash)
        )

        conection.commit()

        return "Cadastro criado com sucesso!"

    except psycopg2.IntegrityError:

        conection.rollback()

        return "E-mail já cadastrado."


def fazer_login(email_digitado, senha_digitada):

    cursor.execute(
        '''SELECT senha_hash
           FROM usuarios
           WHERE email = %s''',
        (email_digitado,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        return "E-mail ou senha incorretos."

    senha_hash_digitada = hashlib.sha256(
        senha_digitada.encode()
    ).hexdigest()

    senha_hash_banco = resultado[0]

    if senha_hash_digitada == senha_hash_banco:
        return "Login realizado com sucesso!"

    return "E-mail ou senha incorretos."


def salvar_verificacao(resultado):

    cursor.execute(
        '''INSERT INTO verificacoes
           (url, status_code, status, response_time)
           VALUES (%s, %s, %s, %s)''',
        (
            resultado["url"],
            resultado["status_code"],
            resultado["status"],
            resultado["response_time"]
        )
    )

    conection.commit()


def buscar_historico():

    cursor.execute(
        '''SELECT *
           FROM verificacoes'''
    )

    resultados = cursor.fetchall()

    return resultados
