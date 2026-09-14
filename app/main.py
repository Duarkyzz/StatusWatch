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

online = 0
tempo_resposta = 0.0

for resultado in historico:
    if resultado['status'] == "Online":
        online += 1;
    if resultado['response_time'] is not None:
        tempo_resposta += resultado['response_time']

tempo_resposta = tempo_resposta / len(historico)
falhas = len(historico) - online

print(f"\nResumo das verificações: ")
print(f"Total de verificações: {len(historico)}")
print(f"Online: {online}")
print(f"Falhas: {falhas}")
print(f"Tempo médio de resposta: {tempo_resposta:.2f} segundos")