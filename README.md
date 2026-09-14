# StatusWatch

> Monitoramento de disponibilidade e desempenho de sites e APIs desenvolvido em Python.

## Sobre o projeto

O **StatusWatch** é uma aplicação de monitoramento desenvolvida em Python com o objetivo de verificar a disponibilidade de sites e serviços, identificar seus códigos de resposta HTTP e medir o tempo necessário para obter uma resposta.

O projeto começou como uma aplicação simples de linha de comando e está sendo desenvolvido de forma progressiva, adicionando novos conceitos e tecnologias conforme sua evolução.

A ideia é transformar o StatusWatch em uma aplicação de monitoramento mais completa, capaz de registrar informações históricas, disponibilizar uma API e apresentar os dados por meio de um dashboard.

---

## Objetivos

O principal objetivo do StatusWatch é construir uma aplicação prática que permita acompanhar a disponibilidade e o desempenho de URLs.

Durante o desenvolvimento, o projeto também serve como prática para conceitos importantes de desenvolvimento backend, como:

- Requisições HTTP
- Tratamento de exceções
- Estruturas de dados
- Funções
- Loops
- Organização de código
- Manipulação de dados
- Persistência de informações
- Desenvolvimento de APIs
- Banco de dados
- Desenvolvimento de aplicações backend

---

## Funcionalidades atuais

Atualmente, o StatusWatch possui as seguintes funcionalidades:

- Entrada de uma URL pelo usuário
- Verificação da disponibilidade da URL
- Realização de requisições HTTP
- Identificação do código de status HTTP
- Identificação de respostas `200`
- Identificação de páginas não encontradas (`404`)
- Tratamento de outros códigos HTTP
- Tratamento de erros de conexão
- Tratamento de timeout
- Medição do tempo de resposta
- Realização de múltiplas verificações
- Armazenamento temporário dos resultados em memória
- Exibição do histórico das verificações

---

## Como funciona

O funcionamento atual da aplicação pode ser resumido da seguinte forma:

```text
Usuário
   │
   │ informa uma URL
   ▼
StatusWatch
   │
   │ realiza uma requisição HTTP
   ▼
Servidor
   │
   │ retorna uma resposta
   ▼
StatusWatch
   │
   ├── verifica o status HTTP
   ├── mede o tempo de resposta
   ├── identifica possíveis erros
   └── registra o resultado
   │
   ▼
Histórico