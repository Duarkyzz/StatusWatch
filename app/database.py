import sqlite3

conection = sqlite3.connect('status_watch.db')

cursor = conection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS verificacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    status_code INTEGER,
    status TEXT NOT NULL,
    response_time REAL NOT NULL
)''')

conection.commit()

print("Tabela 'verificacoes' criada com sucesso!")

def salvar_verificacao(resultado):

    print("Salvando verificação no banco de dados...")
    print(resultado)

    cursor.execute('''INSERT INTO verificacoes (url, status_code, status, response_time)
                      VALUES (?, ?, ?, ?)''',
                   (resultado['url'], resultado['status_code'], resultado['status'], resultado['response_time']))
    conection.commit()