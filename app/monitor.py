import requests
import time


def verificar_url(url):
    start_time = time.time()

    try:
        response = requests.get(url, timeout=5)

        status_code = response.status_code

        if status_code == 200:
            status = "Online"

        elif status_code == 404:
            status = "Página não encontrada"

        else:
            status = f"Status HTTP: {status_code}"

    except requests.exceptions.Timeout:
        status = "Servidor demorou demais para responder"
        status_code = None

    except requests.exceptions.RequestException:
        status = "Não foi possível acessar o servidor"
        status_code = None


    end_time = time.time()
    response_time = end_time - start_time

    resultado = {
        "url": url,
        "status_code": status_code,
        "status": status,
        "response_time": response_time
    }


    return resultado