from tkinter import *
import mysql.connector
import tkinter.messagebox as MessageBox

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="loja"
)

c = con.cursor()
#c.execute('create database loja')
#c.execute('use loja')

# c.execute('''create table produto(
#             codigo int primary key,
#             nome varchar(40) not null,
#             preco decimal(10,2),
#             quantidade int)''')
root = Tk()
root.geometry("500x500")
root.title("Produto")

def inserir():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade = e_quantidade.get()

    if codigo == "" or nome == "":
        MessageBox.showerror("Erro", "Os campos codigo e nome são obrigatorios!")
    else:
        c.execute('insert into produto(codigo,nome,preco,quantidade) values(%s,%s,%s,%s)',(codigo,nome,preco,quantidade))
        con.commit()
        MessageBox.showinfo("Sucesso", "Produto inserido com sucesso!")

        e_codigo.delete(0, END)
        e_nome.delete(0, END)
        e_preco.delete(0, END)
        e_quantidade.delete(0, END)

def excluir():
    codigo = e_codigo.get()
    if codigo == "":
        MessageBox.showerror('Excluir','Informe o codigo!')
    else:
        c.execute('delete from produto where codigo=%s',(codigo,))
        con.commit()
        MessageBox.showinfo("Sucesso", "Produto excluido com sucesso!")
        e_codigo.delete(0, END)

def atualizar():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade = e_quantidade.get()
    if codigo == "":
        MessageBox.showerror('Atualizar','Informe o codigo!')
    else:
        c.execute('update produto set nome=%s,preco=%s,quantidade=%s where codigo=%s',(nome,preco,quantidade,codigo))
        con.commit()
        MessageBox.showinfo("Sucesso", "Produto atualizado com sucesso!")

    e_codigo.delete(0, END)
    e_nome.delete(0, END)
    e_preco.delete(0, END)
    e_quantidade.delete(0, END)

def selecionar():
    codigo = e_codigo.get()
    if codigo == "":
        MessageBox.showerror('Selecionar','Informe o codigo!')
    else:
        c.execute('select * from produto where codigo=%s',(codigo,))
        result = c.fetchall()
        if result:
            for row in result:
                e_nome.delete(0, END)
                e_preco.delete(0, END)
                e_quantidade.delete(0, END)
            MessageBox.showinfo('Selecionar', 'Produto selecionado com sucesso!\n'f'Codigo:{row[0]}\nNome:{row[1]}\nPreço:{row[2]}\nQuantidade:{row[3]}')
        else:
            MessageBox.showerror('Selecionar','Sem Produto !')



Label(root, text="Código").place(x=20, y=30)
Label(root, text="Nome").place(x=20, y=60)
Label(root, text="Preço").place(x=20, y=90)
Label(root, text="Quantidade").place(x=20, y=120)

e_codigo = Entry(root)
e_codigo.place(x=100, y=30)
e_nome = Entry(root)
e_nome.place(x=100, y=60)
e_preco = Entry(root)
e_preco.place(x=100, y=90)
e_quantidade = Entry(root)
e_quantidade.place(x=100, y=120)

Button(root,text='Incluir',command=inserir).place(x=20, y=150)
Button(root,text='Excluir',command=excluir).place(x=80, y=150)
Button(root,text='Alterar',command=atualizar).place(x=140, y=150)
Button(root,text='Consultar',command=selecionar).place(x=200, y=150)


root.mainloop()