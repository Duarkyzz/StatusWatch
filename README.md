# StatusWatch 🔎

StatusWatch é uma aplicação desenvolvida em Python para monitoramento de sites e APIs.

O projeto realiza verificações periódicas em uma URL, identificando seu status HTTP, medindo o tempo de resposta e armazenando os resultados das verificações em um histórico durante a execução da aplicação.

## 🚀 Funcionalidades atuais

- Solicita uma URL ao usuário
- Verifica se o endereço está acessível
- Identifica o código de status HTTP
- Diferencia respostas como:
  - `200` — Online
  - `404` — Página não encontrada
  - Outros códigos HTTP
- Identifica erros de conexão
- Identifica quando o servidor demora demais para responder
- Mede o tempo de resposta da requisição
- Realiza múltiplas verificações da mesma URL
- Armazena os resultados em um histórico durante a execução

## 🛠️ Tecnologias utilizadas

- Python
- Requests
- Time

## 📁 Estrutura do projeto

```text
StatusWatch/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── monitor.py
├── requirements.txt
└── README.md