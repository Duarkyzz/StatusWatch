"""Verificação HTTP independente da interface e do banco."""

import time
from urllib.parse import urlsplit, urlunsplit
import requests


def normalizar_url(url):
    url = url.strip()
    if not url or any(c.isspace() for c in url):
        raise ValueError("Digite uma URL válida, sem espaços.")
    if "://" not in url:
        url = "https://" + url
    try:
        parsed = urlsplit(url)
        port = parsed.port
        if parsed.scheme.lower() not in ("http", "https") or not parsed.hostname:
            raise ValueError
        if parsed.username or parsed.password or port == 0:
            raise ValueError
        host = parsed.hostname.encode("idna").decode("ascii").lower()
        if ":" in host:
            host = f"[{host}]"
        netloc = host + (f":{port}" if port else "")
        return urlunsplit(
            (parsed.scheme.lower(), netloc, parsed.path or "/", parsed.query, "")
        )
    except (ValueError, UnicodeError):
        raise ValueError(
            "Use uma URL HTTP ou HTTPS válida, sem usuário e senha."
        ) from None


def verificar_url(url):
    url = normalizar_url(url)
    inicio = time.perf_counter()
    codigo = None
    try:
        # Não baixa o corpo inteiro: mede o tempo até receber os cabeçalhos.
        with requests.get(
            url, timeout=(5, 8), stream=True, headers={"User-Agent": "StatusWatch/2.0"}
        ) as resposta:
            codigo = resposta.status_code
            if 200 <= codigo < 400:
                status = "Online"
            elif codigo == 404:
                status = "Página não encontrada"
            else:
                status = f"Status HTTP: {codigo}"
    except requests.exceptions.Timeout:
        status = "Servidor demorou demais para responder"
    except requests.exceptions.SSLError:
        status = "Erro no certificado HTTPS"
    except requests.exceptions.RequestException:
        status = "Não foi possível acessar o servidor"
    return {
        "url": url,
        "status_code": codigo,
        "status": status,
        "response_time": time.perf_counter() - inicio,
    }
