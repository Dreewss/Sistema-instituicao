import sqlite3

# CONEXAO
try:
    con = sqlite3.connect("cadastro_alunos.db")
    print("Conexão com banco de dados conectada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

# TABELA
try:
    with con:
        cur = con.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS cursos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nome TEXT,
                        duracao TEXT,
                        preco REAL
                    )
                    """)
        print("Tabela CURSOS criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela:", e)



#Tabela de turmas

# CONEXAO
try:
    con = sqlite3.connect("cadastro_alunos.db")
    print("Conexão com banco de dados conectada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

# TABELA
try:
    with con:
        cur = con.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS turmas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nome TEXT,
                        curso_nome TEXT,
                        data_inicio DATE,
                        FOREIGN KEY(curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
                    )
                    """)
        print("Tabela TURMAS criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela turmas:", e)


#TABELA ALUNOS

# CONEXAO
try:
    con = sqlite3.connect("cadastro_alunos.db")
    print("Conexão com banco de dados conectada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

# TABELA
try:
    with con:
        cur = con.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nome TEXT,
                        email TEXT,
                        telefone TEXT,
                        sexo TEXT,
                        imagem TEXT,
                        data_nascimento DATE,
                        turma_nome TEXT,
                        FOREIGN KEY(turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
                    )
                    """)
        print("Tabela ALUNOS criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela alunos:", e)

