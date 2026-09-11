import requests

import time

url = input("Enter the URL to check: ")

verificacoes = 0

while verificacoes < 5:
    
    start_time = time.time()

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"Online")

        elif response.status_code == 404:
            print(f"Site encontrado, porém a página não foi encontrada.")
        
        else:
            print(f"Site encontrado, mas retornou o status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"🔴 Não foi possível acessar o servidor.")

        if requests.exceptions.Timeout:
            print("🔴 O servidor demorou demais para responder.")
        else:
            print(f"🔴 Não foi possível acessar o servidor.")

    end_time = time.time()
    response_time = end_time - start_time

    print(f"Tempo de resposta: {response_time:.2f} segundos")

    time.sleep(2)

    verificacoes = verificacoes + 1





