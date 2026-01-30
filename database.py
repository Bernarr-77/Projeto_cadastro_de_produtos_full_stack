import sqlite3

def init_db():  
    conexao = sqlite3.connect("database.db",check_same_thread=False)
    cursor = conexao.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS produtos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                quantidade INTEGER,
                valor REAL 
                )
    ''')
    conexao.commit()
    conexao.close

def get_db_connection():
    conn = sqlite3.connect("database.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row 
    try:
        yield conn 
    finally:
        conn.close()