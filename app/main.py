import time

from app.monitor import verificar_url

url = input("Digite a URL que deseja verificar: ")

verificacoes = 0

historico = []

while verificacoes < 5:

    resultado = verificar_url(url)

    historico.append(resultado)

    print(f"Status: {resultado['status']}")
    print(f"Código de status: {resultado['status_code']}")
    print(f"Tempo de resposta: {resultado['response_time']:.2f} segundos")

    time.sleep(2)

    verificacoes += 1


for resultado in historico:
    print(f"URL: {resultado['url']}, Status: {resultado['status']}, Código de status: {resultado['status_code']}, Tempo de resposta: {resultado['response_time']:.2f} segundos")

