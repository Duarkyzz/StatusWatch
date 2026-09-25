# StatusWatch 🔎

Monitor de sites e APIs desenvolvido em **Python**, com interface desktop em **PySide6** e persistência de dados em **PostgreSQL**.

O **StatusWatch** permite monitorar URLs, verificar disponibilidade e respostas HTTP, medir o tempo de resposta e manter um histórico das verificações realizadas por cada usuário.

O projeto começou como uma aplicação via terminal e evoluiu para uma aplicação desktop com autenticação, dashboard e integração com banco de dados.

> 🚀 **StatusWatch Beta — primeira versão lançada em 24/09/2026.**

---

## ✨ Funcionalidades

- 🌐 Monitoramento de sites e APIs
- 📡 Verificação de status HTTP
- ⏱️ Medição do tempo de resposta
- 🛡️ Tratamento de erros e timeout
- 👤 Cadastro e autenticação de usuários
- 🖥️ Interface desktop desenvolvida com PySide6
- 📊 Dashboard para acompanhamento das verificações
- 🗄️ Persistência das verificações em PostgreSQL
- 📋 Histórico de monitoramento por usuário
- 🔄 Suporte à verificação de diferentes URLs
- ☁️ Banco de dados PostgreSQL hospedado no Supabase
- 🔐 Separação dos dados de monitoramento por usuário

---

## 🛠️ Tecnologias

- 🐍 **Python**
- 🌐 **Requests**
- 🖥️ **PySide6**
- 🐘 **PostgreSQL**
- ☁️ **Supabase**
- 🔐 **python-dotenv**
- 🔌 **psycopg2**

---

## 🔄 Como funciona

```text
Usuário cria uma conta ou realiza login
        ↓
Acessa o Dashboard
        ↓
Informa uma URL
        ↓
StatusWatch realiza uma requisição HTTP
        ↓
Analisa o status da resposta
        ↓
Calcula o tempo de resposta
        ↓
Trata erros e timeouts
        ↓
Salva a verificação no PostgreSQL
        ↓
Atualiza o Dashboard
        ↓
Histórico disponível para consulta
```

Cada verificação registra informações como:

- URL monitorada
- Status do serviço
- Código HTTP
- Tempo de resposta
- Data da verificação
- Usuário responsável pela verificação

Os dados são armazenados em um banco **PostgreSQL hospedado no Supabase** e associados à conta autenticada.

---

## 🖥️ Interface

O StatusWatch possui uma interface desktop construída com **PySide6**, utilizando um visual dark e minimalista.

A aplicação é dividida em:

### Login

Permite que usuários cadastrados realizem autenticação para acessar seus dados de monitoramento.

### Cadastro

Permite criar uma nova conta, armazenando os dados do usuário no PostgreSQL.

### Dashboard

Centraliza o monitoramento e apresenta informações como:

- Quantidade de serviços monitorados
- Serviços online
- Serviços offline
- Últimas verificações
- Código HTTP
- Tempo de resposta

### Histórico

Exibe as verificações armazenadas no banco de dados e vinculadas ao usuário autenticado.

---

## 🗄️ Banco de dados

O projeto utiliza **PostgreSQL**, hospedado através do **Supabase**.

As principais informações armazenadas são separadas entre usuários e verificações.

```text
usuarios
├── id
├── email
└── senha_hash

verificacoes
├── id
├── usuario_id
├── url
├── status_code
├── status
├── response_time
└── created_at
```

A associação através de `usuario_id` permite que o histórico de monitoramento seja separado por usuário.

---

## 🔐 Segurança

As credenciais de conexão com o PostgreSQL são carregadas através de variáveis de ambiente e não ficam armazenadas diretamente no código-fonte.

O projeto utiliza:

```text
.env          → credenciais locais (não versionado)
.env.example  → exemplo de configuração
.gitignore    → impede arquivos sensíveis e gerados de serem versionados
```

As senhas dos usuários não são armazenadas diretamente no banco. Antes da persistência, são transformadas em hash.

> ⚠️ O StatusWatch está atualmente em versão **Beta** e não deve ser considerado um sistema pronto para ambientes críticos ou de produção.

---

## 📦 Status do projeto

**Versão atual:** Beta  
**Primeira versão Beta:** 24/09/2026  
**Estado:** Em desenvolvimento

A versão Beta representa a primeira versão funcional do StatusWatch com interface gráfica, autenticação, monitoramento, dashboard, histórico e persistência de dados integrados.

---

## 🎯 Objetivo

O StatusWatch é um projeto de estudo e portfólio criado para aplicar conceitos de desenvolvimento de software e backend em uma aplicação funcional.

Durante seu desenvolvimento são aplicados conceitos como:

- Python
- Requisições HTTP
- Tratamento de exceções
- PostgreSQL
- Persistência de dados
- Autenticação
- Interfaces gráficas
- Integração entre aplicação e banco de dados
- Organização e evolução de código
- Git e GitHub

O projeto também demonstra a evolução de uma aplicação inicialmente executada via terminal para um software desktop integrado a um banco de dados remoto.

---

## 👨‍💻 Autor

**Eduardo Queiroz**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em desenvolvimento backend, Python, APIs, bancos de dados e automações.

> Projeto desenvolvido para aprendizado, prática e construção de portfólio.
