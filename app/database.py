import os
import hashlib
import psycopg2

from dotenv import load_dotenv


# ==========================================================
# CONFIGURAÇÃO DO BANCO
# ==========================================================

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL não foi encontrada no arquivo .env."
    )

conection = psycopg2.connect(DATABASE_URL)


# ==========================================================
# CADASTRO
# ==========================================================

def cadastrar_usuario(email, senha):

    email = email.strip().lower()

    if not email or not senha:
        return "Preencha os dados primeiro!"

    senha_hash = hashlib.sha256(
        senha.encode()
    ).hexdigest()

    cursor = conection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO usuarios (email, senha_hash)
            VALUES (%s, %s)
            """,
            (
                email,
                senha_hash
            )
        )

        conection.commit()

        return "Cadastro criado com sucesso!"

    except psycopg2.IntegrityError:

        conection.rollback()

        return "E-mail já cadastrado."

    except Exception:
        conection.rollback()
        raise

    finally:
        cursor.close()


# ==========================================================
# LOGIN
# ==========================================================

def fazer_login(email_digitado, senha_digitada):

    email_digitado = email_digitado.strip().lower()

    cursor = conection.cursor()

    try:
        cursor.execute(
            """
            SELECT id, senha_hash
            FROM usuarios
            WHERE email = %s
            """,
            (
                email_digitado,
            )
        )

        resultado = cursor.fetchone()

        if resultado is None:
            return None

        usuario_id = resultado[0]
        senha_hash_banco = resultado[1]

        senha_hash_digitada = hashlib.sha256(
            senha_digitada.encode()
        ).hexdigest()

        if senha_hash_digitada == senha_hash_banco:

            return {
                "id": usuario_id,
                "email": email_digitado
            }

        return None

    finally:
        cursor.close()


# ==========================================================
# SALVAR VERIFICAÇÃO
# ==========================================================

def salvar_verificacao(resultado, usuario_id):

    cursor = conection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO verificacoes
            (
                usuario_id,
                url,
                status_code,
                status,
                response_time
            )
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                usuario_id,
                resultado["url"],
                resultado["status_code"],
                resultado["status"],
                resultado["response_time"]
            )
        )

        conection.commit()

    except Exception:
        conection.rollback()
        raise

    finally:
        cursor.close()


# ==========================================================
# HISTÓRICO DO USUÁRIO
# ==========================================================

def buscar_historico(usuario_id):

    cursor = conection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                id,
                url,
                status_code,
                status,
                response_time,
                created_at
            FROM verificacoes
            WHERE usuario_id = %s
            ORDER BY created_at DESC
            """,
            (
                usuario_id,
            )
        )

        return cursor.fetchall()

    finally:
        cursor.close()