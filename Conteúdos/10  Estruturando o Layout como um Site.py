from tkinter import *

r = Tk()
r.geometry('500x500')
r.title('Aula 10')

x = Menu(r)
arquivo_menu = Menu(x,tearoff=0)
x.add_cascade(label='Arquivo',menu=arquivo_menu)
arquivo_menu.add_command(label='Novo')
arquivo_menu.add_command(label='Salvar')
arquivo_menu.add_command(label='Salvar Como')
arquivo_menu.add_command(label='Sair')
r.config(menu=x)

editarMenu = Menu(r,tearoff=0)
x.add_cascade(label='Editar',menu=editarMenu)
editarMenu.add_command(label='Copiar')
editarMenu.add_command(label='Colar')
editarMenu.add_command(label='Voltar')
r.config(menu=x)

inserirMenu = Menu(r,tearoff=0)
x.add_cascade(label='Inserir',menu=inserirMenu)
inserirMenu.add_command(label='Imagens')
inserirMenu.add_command(label='Formas')
inserirMenu.add_command(label='Sair')
r.config(menu=x)

#Abrir nova janela através de um botao - Toplevel(raiz) --------

r = Tk()
r.geometry('500x500')
r.title('Aula 10')

def abrir_janela():
    nova_janela = Toplevel(r)
    nova_janela.title('Aula 10')
    nova_janela.geometry('500x500')
    Label(nova_janela,text='Nova janela').pack()

button = Button(r,text='Abrir Janela Secundária',command=abrir_janela).pack()
#Abrir nova janela sem ação do usuario - má prática -------------

r = Tk()
r.geometry('500x500')
r.title('Aula 10')

nova_janela = Toplevel(r)
nova_janela.title('Janela Secundária')
nova_janela.geometry('400x400')
label=Label(nova_janela,text='Má prática').pack()

#Abrir nova janela através do objeto menu -------------------
r = Tk()
r.geometry('500x500')
r.title('Aula 10')
menu_bar = Menu(r)

def abrir_janela():
    nova_janela = Toplevel(r)
    nova_janela.title('Janela Secundária')
    nova_janela.geometry('400x400')
    Label(nova_janela,text='Nova janela').pack()

novo_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Arquivo',menu=novo_menu)
novo_menu.add_command(label='Nova janela',command=abrir_janela)
r.config(menu=novo_menu)

#Abrir Nova Janela através do Objeto Radiobutton() -------------------

r = Tk()
r.geometry('500x500')
r.title('Aula 10')
frame = Frame(r)
frame.pack()

def abrir_janela():
    nova_janela = Toplevel(r)
    nova_janela.title('nova janela')
    nova_janela.geometry('400x400')
    Label(nova_janela,text='Nova janela').pack()

s = IntVar()      

r1 =Radiobutton(frame,text='Opção1',variable=s,value=1).pack()
r2 = Radiobutton(frame,text='Nova Janela',variable=s,value=2,command=abrir_janela).pack()

#Criando um site com Tkinter --------------------------

janela = Tk()
janela.geometry('500x500')
janela.title('Site')

div_cabecalho = Frame(janela,bg='gray',width=800,height=50)
div_cabecalho.pack()

div_conteudo = Frame(janela,bg='white',width=800,height=400)
div_conteudo.pack()

div_rodape = Frame(janela,bg='lightgray',width=800,height=50)
div_rodape.pack()

label_titulo = Label(div_cabecalho,text='Meu Site')
label_titulo.pack(pady=20)

label_conteudo = Label(div_conteudo,text='Site')
label_conteudo.pack(pady=50)

label_rodape = Label(div_rodape,text='Direitos reservados')
label_rodape.pack(pady=10)

janela.mainloop()