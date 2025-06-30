from tkinter import *

i = Tk()  #cria a instância da janela
i.title('Janela Principal') #inserir titulo na janela
i.geometry('600x400') #definir o tamanho da janela
#i.resizable(False,0) bloquear a janela, pode ser 0 e 1 ou False e True
#i.state('zoomed') abre a janela em tela cheia
#i.state('iconic') abre a janela minimizada
i['bg']='#CECECE'  #definir a cor de fundo da janela
i.minsize(300, 200) #menor tamanho da janela
i.maxsize(900, 600) #maior tamanho da janela

#Entry() - caixa de entrada --------------------------------

e = Entry(i)
e.pack()

#Button() - inserir um botão na janela -------------------

btn = Button(i,text='Cadastrar',font='Verdana 10 bold')
btn.pack()

#Label - rotulo na janela ----------------------------------
def botao_clicado():
    label.config(text='Olá,você clicou no botao')

btn = Button(i,
       text='Clique aqui!',
       font = 'Arial 10 italic',
       fg = 'white', #cor da fonte
       bg = '#4CAF50',#cor de fundo
       relief = 'raised',#tipo de borda(flat,raised,sunken,solid,groove,double,ridge)
       bd = 3, #definir o tamanho da borda
       padx = 20, #espaço na horizontal
       pady = 20, #espaço vertical
       activebackground = '#45A049',#cor de fundo quando presionada
       activeforeground = 'red',#cor da fonte quando presionada
       command = botao_clicado
    )
btn.pack(pady=20)#espaço vetical entre o botao e o rotulo

label = Label(i,
              bg='#CECECE',
              padx=30,
              pady=20,
              fg='white',
              width=20 #largura do label
 )
label.pack(pady=10) #espaço entre o label e a janela

#Sistema grid(linha,grid) ------------------------------------------------

x1 = Label(i,text='Teste 1',font='Arial 10 bold',bg='blue')
x2 = Label(i,text='Teste 2',font='Arial 10 bold',bg='pink')
x3 = Label(i,text='Teste 3',font='Arial 10 bold',bg='orange')

x1.grid(row=0,column=0,padx=10,pady=10)
x2.grid(row=1,column=0,padx=10,pady=10)
x3.grid(row=2,column=0,padx=10,pady=10)

#--------------------------------------------------------------
label_nome = Label(i,text='Nome:',font='Arial 10 bold',bg='#CECECE')
label_nome.grid(row=0,column=0,padx=10,pady=10)

entry_nome=Entry(i)
entry_nome.grid(row=0,column=1,padx=10,pady=10)

label_email = Label(i,text='E_mail:',font='Arial 10 bold',bg='#CECECE')
label_email.grid(row=1,column=0,padx=10,pady=10)

entry_email=Entry(i)
entry_email.grid(row=1,column=1,padx=10,pady=10)

def mostrar_informacoes():
    nome=entry_nome.get()
    email=entry_email.get()
    res_label.config(text=f'Nome: {nome} \n Email: {email}')

btn = Button(i,text='Mostrar informação',command=mostrar_informacoes)
btn.grid(row=2,column=0,columnspan=2)

res_label=Label(i,bg='#CECECE')
res_label.grid(row=3,column=0,columnspan=2)

#Checkbutton() - seleção multipla -----------------------------------

x = Label(i,bg='#CECECE',text='Escolha o seu esporte de preferência',font='Arial 10 bold')
a1 = Checkbutton(i,text='Natação',bg='#CECECE')
a2 = Checkbutton(i,text='Basquete',bg='#CECECE')
a3 = Checkbutton(i,text='Volei',bg='#CECECE')
a4 = Checkbutton(i,text='Futebol',bg='#CECECE')
a5 = Checkbutton(i,text='Tênis',bg='#CECECE')
x.place(x=10,y=10)
a1.place(x=10,y=40)
a2.place(x=90,y=40)
a3.place(x=170,y=40)
a4.place(x=240,y=40)
a5.place(x=320,y=40)

#----------------------------------------------------------------
def mostrar_selecionados():
    selecionados = []
    if futebol_var.get():
        selecionados.append('Futebol')
    if volei_var.get():
        selecionados.append('Volei')
    if basquete_var.get():
        selecionados.append('Basquete')
    if natacao_var.get():
        selecionados.append('Natação')
    if tenis_var.get():
        selecionados.append('Tênis')
    result_label.config(text="Esporte selecionado: "+" ☻ ".join(selecionados))

futebol_var = IntVar()
volei_var = IntVar()
basquete_var=IntVar()
natacao_var = IntVar()
tenis_var=IntVar()

futebol = Checkbutton(i,text='futebol',bg='#CECECE',variable=futebol_var)
volei = Checkbutton(i,text='volei',bg='#CECECE',variable=volei_var)
basquete = Checkbutton(i,text='basquete',bg='#CECECE',variable=basquete_var)
natacao = Checkbutton(i,text='natação',bg='#CECECE',variable=natacao_var)
tenis = Checkbutton(i,text='tenis',bg='#CECECE',variable=tenis_var)

futebol.place(x=10,y=40)
volei.place(x=90,y=40)
basquete.place(x=170,y=40)
natacao.place(x=240,y=40)
tenis.place(x=320,y=40)

mostrar_button = Button(i,text='Mostrar selecionados',command=mostrar_selecionados)
mostrar_button.place(x=10,y=70)

result_label = Label(i,bg='#CECECE',text='Esporte(s) selecionado(s):Nenhum')
result_label.place(x=10,y=100)

#Radiobutton() - seleção simples -------------------------------------
valor = IntVar()
r1 = Radiobutton(i,text='Opção 1',value=1,variable=valor,bg='#CECECE')
r2 = Radiobutton(i,text='Opção 2',value=2,variable=valor,bg='#CECECE')
r3 = Radiobutton(i,text='Opção 3',value=3,variable=valor,bg='#CECECE')

r1.pack()
r2.pack()
r3.pack()

#Listbox() - criar uma lista ------------------------------------

lista = Listbox(i,bg='#CECECE')
lista.insert(0,'Ac')
lista.insert(1,'Al')
lista.insert(2,'Ap')
lista.insert(END,'RJ')
lista.insert(END,'MG')
lista.insert(END,'SP')
lista.pack()

#---------------------------------------------------------
lista = Listbox(i,bg='#CECECE')
estado = ['AC','Al','Ap']
for e in estado:
    lista.insert(END,e)
lista.pack()









i.mainloop()