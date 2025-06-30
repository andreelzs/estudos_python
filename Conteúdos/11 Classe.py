'''class Aluno:
    def __init__(self, nome, idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f'Olá!Meu nome é {self.nome}, tenho {self.idade} anos e curso {self.curso}.')

    def maioridade(self):
        if self.idade >= 18:
            print(f'{self.nome} é maior de idade.')
        else:
            print(f'{self.nome} é menor de idade.')

aluno1 = Aluno('Julio', 21,'Python')
aluno1.apresentar()
aluno2 = Aluno('Joana', 5,'C++')
aluno2.apresentar()
aluno1.maioridade()

#Verificar se o aluno esta aprovado -----------------------------

class Aluno:
    def __init__(self, nome, idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []

    def apresentar(self):
        print(f'Olá!Meu nome é {self.nome}, tenho {self.idade} anos e curso {self.curso}.')

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print('Nota inválida.Insira uma nota entre 0 e 10.')

    def calcular_media(self):
        if len(self.notas) == 0:
            return
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        print(f'Media do {self.nome} : {media:.2f}')
        if media >= 7:
            print(f'{self.nome} foi aprovado.')
        else:
            print(f'{self.nome}  foi reprovado.')

aluno1 = Aluno('Julio', 21,'Python')

aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(2.5)
aluno1.adicionar_nota(4.0)
aluno1.verificar_aprovacao()

aluno2.maioridade()
aluno1.apresentar()

#exemplo com menu --------------------------------------------
class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []

    def apresentar(self):
        print(f'Olá!Meu nome é {self.nome}, tenho {self.idade} anos e curso {self.curso}.')

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f'Nota {nota} foi adicionado.')
        else:
            print('Nota inválida.Insira uma nota entre 0 e 10.')

    def calcular_media(self):
        if len(self.notas) == 0:
            return
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        print(f'Media do {self.nome} : {media:.2f}')
        if media >= 7:
            print('Aprovado')
        else:
            print('Reprovado.')

def menu():
    aluno = None
    while True:
        print('\n======Menu======')
        print('1 - Cadastrar o aluno')
        print('2 - Cadastrar nota')
        print('3 - Verificar aprovacao')
        print('4 - Mostrar dados do aluno')
        print('5 - Sair')

        opcao = input('Escolha uma opcao(1-5): ').strip()
        if not opcao:
            print('Entrada vazia.Digite uma opção')
            continue
        if opcao == '1':
            nome = input('Nome: ').strip()
            idade = input('Idade: ').strip()
            curso = input('Curso: ').strip()
            aluno = Aluno(nome, idade, curso)
            print('Aluno cadastrado com sucesso!')

        elif opcao == '2':
            if aluno:
                try:
                    nota = float(input('Digite sua nota(0-10): '))
                    aluno.adicionar_nota(nota)
                except ValueError:
                    print('Nota inválida')
            else:
                print('Cadastre o aluno primeiro')

        elif opcao == '3':
            if aluno:
                aluno.verificar_aprovacao()
            else:
                print('Nenhum aluno cadastrado!')

        elif opcao == '4':
            if aluno:
                aluno.apresentar()
                print('Notas:',aluno.notas)
            else:
                print('Nenhum aluno cadastrado!')

        elif opcao == '5':
            print('Encerrando...')
            break
        else:
            print('opção invalida. Tente novamente.')

menu()'''

import tkinter as tk
from tkinter import messagebox

class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            return True
        return False

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        return media >= 7, media

class App:
    def __init__(self,root):
        self.root = root
        self.root.title('Aluno')
        self.aluno = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text='Nome: ').grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(self.root, text='Idade: ').grid(row=1, column=0)
        self.idade_entry = tk.Entry(self.root)
        self.idade_entry.grid(row=1, column=1)

        tk.Label(self.root, text='Curso: ').grid(row=2, column=0)
        self.curso_entry = tk.Entry(self.root)
        self.curso_entry.grid(row=2, column=1)

        tk.Button(self.root,text='Cadastrar Aluno',command=self.cadastrar_aluno).grid(row=3,columnspan=2,pady=10)

        tk.Label(self.root,text='Nota: ').grid(row=4, column=0)
        self.nota_entry = tk.Entry(self.root)
        self.nota_entry.grid(row=4, column=1)

        tk.Button(self.root,text='Adicionar nota: ',command=self.adicionar_nota).grid(row=5,columnspan=2,pady=10)

        tk.Button(self.root,text='Media/Situação',command=self.mostrar_media).grid(row=6,columnspan=2,pady=5)
        tk.Button(self.root,text='Mostrar dados',command=self.mostrar_dados).grid(row=7,columnspan=2,pady=5)

    def cadastrar_aluno(self):
        nome = self.nome_entry.get().strip()
        idade = self.idade_entry.get().strip()
        curso = self.curso_entry.get().strip()

        if nome and idade.isdigit() and curso:
            self.aluno = Aluno(nome, int(idade), curso)
            messagebox.showinfo('Cadastro!', f'Aluno {nome} cadastrado com sucesso!')
        else:
            messagebox.showwarning('Erro!Preencha todos os campos!')

    def adicionar_nota(self):
        if not self.aluno:
            messagebox.showwarning('Erro!Cadastre um aluno primeiro')
            return
        nota = self.nota_entry.get()
        try:
            nota = float(nota)
            if self.aluno.adicionar_nota(nota):
                messagebox.showinfo('Nota: ',f'Nota {nota} adicionada com sucesso!')
                self.nota_entry.delete(0, tk.END)
            else:
                messagebox.showerror('Erro!Nota deve estar entre 0 e 10!')
        except ValueError:
            messagebox.showwarning('Digite um numero válido!')

    def mostrar_media(self):
        if not self.aluno:
            messagebox.showwarning('erro!Cadastre um aluno primeiro')
            return
        aprovado,media = self.aluno.verificar_aprovacao()
        status = 'aprovado' if aprovado else 'reprovado'
        messagebox.showinfo('Resultado',f'Media : {media:.2f}\n Situação: {status}')

    def mostrar_dados(self):
        if not self.aluno:
            messagebox.showwarning('erro!Cadastre um aluno primeiro')
            return
        dados = (
            f'Nome: {self.aluno.nome}\n'
            f'Idade: {self.aluno.idade}\n'
            f'Curso: {self.aluno.curso}\n'
            f'Nota: {self.aluno.notas}\n'
            f'Media: {self.aluno.calcular_media()}\n'
        )
        messagebox.showinfo('dados Aluno', dados)
root = tk.Tk()
app = App(root)
root.mainloop()