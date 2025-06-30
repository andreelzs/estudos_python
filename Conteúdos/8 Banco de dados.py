from os.path import exists

import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="aula8"
)
x = conexao.cursor()

#criar base de dados -----------------------------------

#x.execute('create database if not exists aula8')

#mostrar todas as bases de dados existentes ------------
x.execute("show databases")
for i in x:
    print(i)
#-----------------------------------------------
x.execute('use aula8')

#criar tabela - create table ------------------
x.execute('''create table if not exists aluno(
          matricula int primary key auto_increment,
          nome varchar(20) not null,
          idade int(3),
          email varchar(20))''')

#mostrar todas as tabelas do banco de dados-------

x.execute("show tables")
for i in x:
    print(i)

#mostra a estrutura da tabela  - desc ou describe -----------------

x.execute('desc aluno')
for i in x:
    print(i)

#inserir dados na tabela - insert into nome(atributos) values(%s) ---

a = 'insert into aluno(nome,idade,email) values ("Thereza",30,"teste@gmail.com")'
x.execute(a)
conexao.commit()
print(x.rowcount,'registro(s) inserido(s)')

#multiplos valores ---------------------------------------------

v = [
    ("Tatiana",32,"teste1@gmail.com"),
    ("Paulo",12,"teste2@gmail.com"),
    ("Talmo",34,"teste3@gmail.com"),
    ("Maria",78,"teste4@gmail.com"),
    ("Manoel",3,"teste5@gmail.com"),
    ("Clara",89,"teste6@gmail.com"),
    ("Julia",23,"teste7@gmail.com"),
]
x.executemany('insert into aluno(nome,idade,email) values (%s,%s,%s)',v)
conexao.commit()
print(x.rowcount,'registro(s) inserido(s)')

#seleção simples - select * from nome da tabela -----------

x.execute('select * from aluno')
r = x.fetchall()
print('Todos os dados dos alunos:')
for i in r:
    print(i)
#seleção nome e idade --------------------------------------

x.execute('select nome,idade from aluno')
r = x.fetchall()
print('Nome e idade dos alunos:')
for i in r:
    print(i)

#seleção trazendo apenas um registro(fetchone) -------------

x.execute('select nome,idade from aluno')
r = x.fetchone()
print('Primeiro nome e idade dos alunos:')
for i in r:
    print(i)

#seleção com condição - where ------------------------------

x.execute('select nome,idade from aluno where idade > 20')
r = x.fetchall()
print('nome e idade dos alunos:')
for i in r:
    print(i)

#seleção com ordenação - order by Asc /Desc -------------------

x.execute('select nome,idade from aluno order by nome')
r = x.fetchall()
print('Ordenado por nome (A-Z)')
for i in r:

#--------------------------------------------------------
x.execute('select nome,idade from aluno order by nome desc')
r = x.fetchall()
print('Ordenado por nome (Z-A)')
for i in r:
    print(i)

#delete - deletar 1 arquivo -------------------

x.execute('Delete from aluno where matricula=1')
conexao.commit()
print(x.rowcount,'registro(s) deletado(s)')

#deletar multiplos valores com in ------------

s='delete from aluno where matricula in (%s,%s)'
x.execute(s,(10,12))
conexao.commit()
print(x.rowcount,'registro(s) deletado(s)')

#deletar com intervalo bbetween -----------------------

s1 = 'delete from aluno where matricula between %s and %s'
x.execute(s1,(13,15))
conexao.commit()
print(x.rowcount,'registro(s) deletado(s)')

#update - atualizar -------------------------------------

x.execute('update aluno set nome="Tatiana Viana" where matricula=9')
conexao.commit()
print(x.rowcount,'registro(s) atualizado(s)')