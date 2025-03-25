from tkinter import *

i = Tk()
i.title('Janela Principal')
i.geometry('600x400')
#i.resizable(False,0)
#i.state('zoomed')
#i.state('iconic')
i.config(bg='light blue') #or i['bg']= 'light blue'
i.minsize(300, 200)
i.maxsize(900, 600)
i.wm_iconbitmap('Davi.ico')
