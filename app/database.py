import sqlite3

conection = sqlite3.connect('database.db')

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