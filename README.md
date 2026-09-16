# StatusWatch 🔎

Monitor de sites e APIs desenvolvido em Python.

O **StatusWatch** é uma aplicação desenvolvida para monitorar URLs, verificar o status de respostas HTTP, medir o tempo de resposta e armazenar o histórico das verificações.

O projeto está sendo desenvolvido de forma progressiva, começando pelo monitoramento via terminal e evoluindo para uma aplicação desktop completa.

---

## ✨ Funcionalidades

- 🌐 Monitoramento de URLs
- 📡 Verificação de status HTTP
- ⏱️ Medição do tempo de resposta
- 🔄 Múltiplas verificações
- 🛡️ Tratamento de erros e timeout
- 🗄️ Armazenamento das verificações em banco de dados
- 📋 Consulta do histórico de verificações

---

## 🛠️ Tecnologias

### Atualmente

- 🐍 Python
- 🌐 Requests
- 🗄️ SQLite

### Em desenvolvimento

- 🖥️ PySide6 — Interface gráfica
- ⚡ FastAPI — API
- 🧵 Threads / Async — Monitoramento em paralelo

### Futuro

- 🐘 PostgreSQL
- 🔔 Sistema de notificações
- 📦 PyInstaller — Aplicação executável
- 👤 Sistema de usuários

---

## 🔄 Como funciona

O fluxo principal do StatusWatch atualmente funciona da seguinte forma:

    Usuário informa uma URL
            ↓
    StatusWatch realiza uma requisição HTTP
            ↓
    Analisa o status da resposta
            ↓
    Calcula o tempo de resposta
            ↓
    Trata possíveis erros e timeouts
            ↓
    Salva a verificação no SQLite
            ↓
    Permite consultar o histórico

---

## 🗺️ Roadmap

### ✅ Concluído

- [x] Receber URL do usuário
- [x] Realizar requisições HTTP
- [x] Verificar status da resposta
- [x] Medir tempo de resposta
- [x] Realizar múltiplas verificações
- [x] Tratar erros de conexão
- [x] Implementar timeout
- [x] Criar banco de dados SQLite
- [x] Registrar verificações
- [x] Consultar histórico

### 🔨 Em desenvolvimento

- [ ] Separar melhor as responsabilidades do projeto
- [ ] Cadastro de múltiplas URLs
- [ ] Monitoramento automático
- [ ] Interface gráfica com PySide6
- [ ] Exibição do histórico na interface
- [ ] Gráficos de tempo de resposta

### 🔮 Futuro

- [ ] Monitoramento de várias URLs simultaneamente
- [ ] Threads / Async
- [ ] API com FastAPI
- [ ] Sistema de usuários e autenticação
- [ ] Sistema de notificações
- [ ] Migração para PostgreSQL
- [ ] Gerar aplicativo executável para Windows
- [ ] Deploy

---

## 🎯 Objetivo do projeto

O StatusWatch está sendo desenvolvido como um projeto de estudo e portfólio, com o objetivo de aplicar conceitos de:

- Python
- Programação orientada a objetos
- Requisições HTTP
- Tratamento de exceções
- Banco de dados
- Arquitetura de aplicações
- APIs
- Interfaces gráficas
- Concorrência e monitoramento

A ideia é evoluir o projeto gradualmente, entendendo e implementando cada parte do sistema.

---

## 👨‍💻 Autor

**Eduardo Queiroz**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em desenvolvimento backend e Python.

> Projeto desenvolvido para aprendizado, prática e construção de portfólio.
