"""Modo terminal preservado, agora com login para associar o histórico."""

import time
from getpass import getpass
from app.monitor import verificar_url
from app.database import fazer_login, salvar_verificacao


def main():
    try:
        user = fazer_login(input("E-mail: "), getpass("Senha: "))
        if not user:
            print("E-mail ou senha incorretos.")
            return 1
        url = input("URL: ")
        history = []
        for i in range(5):
            result = verificar_url(url)
            salvar_verificacao(result, user["id"])
            history.append(result)
            print(
                f"{result['status']} | HTTP {result['status_code']} | {result['response_time']:.2f}s"
            )
            if i < 4:
                time.sleep(2)
        online = sum(r["status"] == "Online" for r in history)
        print(f"Total: 5 | Online: {online} | Falhas: {5 - online}")
        print(f"Tempo médio: {sum(r['response_time'] for r in history) / 5:.2f}s")
        return 0
    except (ValueError, KeyboardInterrupt):
        print("Operação cancelada ou configuração/URL inválida.")
        return 1
    except Exception:
        print("Falha de conexão ou banco. Confira seu .env e a migração SQL.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
