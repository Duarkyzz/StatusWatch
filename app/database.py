"""PostgreSQL: conexão curta por operação, segura para tarefas de fundo."""

import re
from contextlib import contextmanager
import psycopg2
from app.config import database_url
from app.security import gerar_hash, verificar_senha


@contextmanager
def conectar():
    conn = psycopg2.connect(
        database_url(), connect_timeout=8, options="-c statement_timeout=15000"
    )
    try:
        with conn:
            with conn.cursor() as cursor:
                yield cursor
    finally:
        conn.close()


def cadastrar_usuario(email, senha):
    email = email.strip().lower()
    if not email or not senha:
        return "Preencha os dados primeiro!"
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        return "Digite um e-mail válido."
    if len(senha) < 8:
        return "Use uma senha com pelo menos 8 caracteres."
    senha_hash = gerar_hash(senha)
    try:
        with conectar() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (email, senha_hash) VALUES (%s, %s)",
                (email, senha_hash),
            )
        return "Cadastro criado com sucesso!"
    except psycopg2.errors.UniqueViolation:
        return "E-mail já cadastrado."


def fazer_login(email_digitado, senha_digitada):
    email = email_digitado.strip().lower()
    if not email or not senha_digitada:
        return None
    with conectar() as cursor:
        cursor.execute("SELECT id, senha_hash FROM usuarios WHERE email = %s", (email,))
        row = cursor.fetchone()
        if row is None or not verificar_senha(senha_digitada, row[1]):
            return None
        if not row[1].startswith("pbkdf2_sha256$"):
            cursor.execute(
                "UPDATE usuarios SET senha_hash = %s WHERE id = %s",
                (gerar_hash(senha_digitada), row[0]),
            )
        return {"id": row[0], "email": email}


def salvar_verificacao(resultado, usuario_id):
    if not usuario_id:
        raise ValueError("Faça login antes de salvar uma verificação.")
    with conectar() as cursor:
        cursor.execute(
            """INSERT INTO verificacoes
            (usuario_id, url, status_code, status, response_time)
            VALUES (%s, %s, %s, %s, %s)""",
            (
                usuario_id,
                resultado["url"],
                resultado["status_code"],
                resultado["status"],
                resultado["response_time"],
            ),
        )


def buscar_historico(usuario_id):
    with conectar() as cursor:
        cursor.execute(
            """SELECT id, url, status_code, status, response_time, created_at
            FROM verificacoes WHERE usuario_id = %s
            ORDER BY created_at DESC NULLS LAST, id DESC LIMIT 1000""",
            (usuario_id,),
        )
        return cursor.fetchall()


def buscar_ultimos(usuario_id):
    """Um registro por URL, mesmo se ela não estiver nas mil consultas recentes."""
    with conectar() as cursor:
        cursor.execute(
            """SELECT DISTINCT ON (url)
            id, url, status_code, status, response_time, created_at
            FROM verificacoes WHERE usuario_id = %s
            ORDER BY url, created_at DESC NULLS LAST, id DESC""",
            (usuario_id,),
        )
        return cursor.fetchall()
