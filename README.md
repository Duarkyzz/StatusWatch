# StatusWatch 🔎

Monitor de sites e APIs desenvolvido em **Python**, com armazenamento em **PostgreSQL** e interface desktop em desenvolvimento.

O **StatusWatch** monitora URLs, verifica respostas HTTP, mede o tempo de resposta e mantém um histórico das verificações.

O projeto começou como uma aplicação via terminal e está evoluindo para uma aplicação desktop com autenticação, monitoramento e histórico integrado.

---

## ✨ Funcionalidades

- 🌐 Monitoramento de sites e APIs
- 📡 Verificação de status HTTP
- ⏱️ Medição do tempo de resposta
- 🛡️ Tratamento de erros e timeout
- 🔄 Múltiplas verificações
- 🗄️ Histórico de verificações em PostgreSQL
- 👤 Cadastro e autenticação de usuários
- 🖥️ Interface desktop com PySide6 em desenvolvimento

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
Usuário informa uma URL
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
Histórico disponível para consulta
```

A aplicação utiliza um banco **PostgreSQL hospedado no Supabase**. As credenciais de conexão são mantidas localmente através de variáveis de ambiente e não fazem parte do repositório.

---

## 🗺️ Roadmap

### ✅ Concluído

- [x] Monitoramento de URLs
- [x] Requisições HTTP
- [x] Status HTTP
- [x] Tempo de resposta
- [x] Tratamento de erros e timeout
- [x] Histórico de verificações
- [x] Migração de SQLite para PostgreSQL
- [x] Banco PostgreSQL hospedado no Supabase
- [x] Estrutura inicial de usuários
- [x] Cadastro e validação no banco
- [x] Estrutura inicial da interface com PySide6

### 🔨 Em desenvolvimento

- [ ] Integrar cadastro à interface
- [ ] Integrar login à interface
- [ ] Finalizar navegação entre Login, Cadastro e Dashboard
- [ ] Aplicar interface dark e minimalista
- [ ] Exibir histórico no Dashboard
- [ ] Cadastro e gerenciamento de múltiplas URLs

### 🔮 Próximos passos

- [ ] Monitoramento automático
- [ ] Monitoramento simultâneo de múltiplas URLs
- [ ] Gráficos de tempo de resposta
- [ ] API com FastAPI
- [ ] Sistema de notificações
- [ ] Melhorias de segurança na autenticação
- [ ] Gerar executável para Windows
- [ ] Deploy

---

## 🔐 Segurança

As credenciais do PostgreSQL são armazenadas através de variáveis de ambiente.

O repositório utiliza:

```text
.env          → credenciais locais (não versionado)
.env.example  → exemplo de configuração
.gitignore    → impede arquivos sensíveis e gerados de serem versionados
```

Nenhuma senha ou credencial do banco deve ser adicionada diretamente ao código.

> A autenticação ainda está em desenvolvimento e não deve ser considerada pronta para uso em produção.

---

## 🎯 Objetivo

O StatusWatch é um projeto de estudo e portfólio criado para aplicar conceitos de desenvolvimento backend na prática, incluindo:

- Python
- Requisições HTTP
- Tratamento de exceções
- PostgreSQL
- Persistência de dados
- Autenticação
- Interfaces gráficas
- Organização e evolução de aplicações

O objetivo é transformar gradualmente um monitor simples de URLs em uma aplicação completa de monitoramento.

---

## 👨‍💻 Autor

**Eduardo Queiroz**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em desenvolvimento backend e Python.

> Projeto desenvolvido para aprendizado, prática e construção de portfólio.