import sqlite3 as lite
from indb import con  

#TABELA CURSOS-------------------------------------------------------------------------------------------------------------------


# cursos (C do CRUD)
def criar_cursos(i):
    try:
        with con:
            cur = con.cursor()
            query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?, ?, ?)"
            cur.execute(query, i)
            print("Curso inserido com sucesso!")
    except lite.Error as e:
        print("Erro ao inserir curso:", e)


#criar_cursos(["Python", "2 semanas", 50])

#cursos (R do CRUD)
def ver_cursos():
    lista = []
    try:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Cursos")
            linha = cur.fetchall()

            for i in linha:
                lista.append(i)
    except lite.Error as e:
        print("Erro ao recuperar cursos:", e)
    return lista


#print(ver_cursos())


#ATUALIZAR (UPDATE U) CRUD

def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome = ? , duracao = ? , preco = ? WHERE id=?"
        cur.execute(query, i)

#DELETAR (DELETE D) CRUD
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id = ?"
        cur.execute(query, i)



#TABELA DE TURMAS -------------------------------------------------------------------------------------------------------------------

#CRIAR TURMAS (INSERT )

def criar_turmas(i):
    with con:
        cur=con.cursor()
        query = "INSERT INTO Turmas (nome,cursos_nome, data_inicio) VALUES (?,?,?)"
        cur.execute (query, i)


#(READ R)

def ver_turmas():
    lista = []
    with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Turmas")
            linha = cur.fetchall()

            for i in linha:
                lista.append(i)

    return lista

#atualizar turmas (update U)

def atualizar_turma(i):
    with con:
        cur = con.cursor()
        query = "UPDATE turma SET nome = ? , cursos_nome = ? , data_inicio = ? WHERE id=?"
        cur.execute(query, i)


#DELETAR TURMAS

def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id = ?"
        cur.execute(query, i)



#TABELA ALUNOS -------------------------------------------------------------------------------------------------------------------
def criar_alunos(i):
        with con:
            cur = con.cursor()
            query = "INSERT INTO Alunos (nome,email, telefone ,sexo,imagem, data_nascimento, turma_nome) VALUES (?, ?, ?,?,?,?,?)"
            cur.execute(query, i)

#(READ R)

def ver_alunos():
    lista = []
    with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Alunos")
            linha = cur.fetchall()

            for i in linha:
                lista.append(i)
    return lista


#atualizar Alunos (UPDATE U)

def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE turma SET nome=?,email=?, telefone=? ,sexo=?,imagem=?, data_nascimento=?, turma_nome=? WHERE id= ?"
        cur.execute(query, i)


#DELETAR Alunos (DELETE D)

def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Alunos WHERE id = ?"
        cur.execute(query, i)
