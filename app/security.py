"""Senhas novas usam PBKDF2; contas SHA-256 antigas migram ao entrar."""

import hashlib
import hmac
import secrets

ITERATIONS = 600_000


def gerar_hash(senha):
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", senha.encode(), salt.encode(), ITERATIONS
    ).hex()
    return f"pbkdf2_sha256${ITERATIONS}${salt}${digest}"


def verificar_senha(senha, armazenada):
    try:
        if armazenada.startswith("pbkdf2_sha256$"):
            _, iterations, salt, digest = armazenada.split("$")
            iterations = int(iterations)
            if not 100_000 <= iterations <= 2_000_000:
                return False
            atual = hashlib.pbkdf2_hmac(
                "sha256", senha.encode(), salt.encode(), iterations
            ).hex()
        else:
            digest = armazenada
            atual = hashlib.sha256(senha.encode()).hexdigest()
        return hmac.compare_digest(atual, digest)
    except (ValueError, AttributeError, TypeError):
        return False
