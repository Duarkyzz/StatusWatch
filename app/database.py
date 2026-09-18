import sqlite3
import hashlib

conection = sqlite3.connect('status_watch.db')

cursor = conection.cursor()

# Tabela das verificações

cursor.execute('''CREATE TABLE IF NOT EXISTS verificacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    status_code INTEGER,
    status TEXT NOT NULL,
    response_time REAL NOT NULL
)''')

# Tabela das contas registradas

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL
)''')

conection.commit()

def fazer_login(email_digitado, senha_digitada):

    # 1. Busca o usuário apenas pelo e-mail (Seguro contra SQL Injection)

    cursor.execute("SELECT senha_hash FROM usuarios WHERE email = ?", (email_digitado,))
    resultado = cursor.fetchone()

    # 2. Se o e-mail não existir no banco

    if resultado is None:
        return "E-mail ou senha incorretos."

    # 3. Transforma a senha digitada em HASH para comparação

    senha_hash_digitada = hashlib.sha256(senha_digitada.encode()).hexdigest()
    senha_hash_banco = resultado[0]

    if senha_hash_digitada == senha_hash_banco:
        return "Login efetuado com sucesso"
    else:
        return "E-mail ou senha incorretos."

def cadastrar_usuario(email, senha, cadastros):

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    
    cursor.execute ('''INSERT INTO cadastrar_usuario (email, senha)
                      VALUES (?, ?)''',
                   (cadastros["email"], cadastros["senha"]))

def salvar_verificacao(resultado):

    cursor.execute('''INSERT INTO verificacoes (url, status_code, status, response_time)
                      VALUES (?, ?, ?, ?)''',
                   (resultado['url'], resultado['status_code'], resultado['status'], resultado['response_time']))
    conection.commit()

def buscar_historico():

    cursor.execute('''SELECT * FROM verificacoes''')

    resultados = cursor.fetchall()

    return resultados