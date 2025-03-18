#dicionário - nome do dicionario = {'chave':'valor} -------------
#criar dicionario vazio
d = {}
e = dict()
print(d)
print(e)
f = []
g = ()
print(type(d))
print(type(f))
print(type(g))

#-----------------------------------------------------------

if not d:
    print('O dicionario está vazio')
else:
    print('O dicionario não está vazio')

#-----------------------------------------------------------

aluno = {
    'nome': 'Thereza',
    'idade': 27,
    'sexo': 'F',
    'email': 'teste2gmail.com'
}
print(aluno)
print('Nome:',aluno['nome'])
print('Idade: ',aluno['idade'])

aluno['nome'] = 'Thereza Gondim'
print(aluno)

aluno['nacionalidade'] = 'Brasileira'
print(aluno)

del aluno['sexo']
print(aluno)

#keys() - mostra a chave
#values() - mostra os valores
#items() - mostra a chave e os valores

filme = {'titulo':'Moana','ano':2017,'diretor':'Jonh Musker'}
print(filme)
print(filme.keys())
print(filme.values())
print(filme.items())

#------------------------------------------------------------

d1 = {'a':1,'b':2,'c':3}
for c in d1.values():
    print(f'Valor: {c}')

#------------------------------------------------------------

notas = {}    # notas = dict()
notas = {
    'G1':float(input('Digite a primeira nota: ')),
    'G2':float(input('Digite a segunda nota: ')),
    'G3':float(input('Digite a terceira nota: '))
}
for c,v in notas.items():
    print(f'{c} Nota: {v}')

#----------------------------------------------------------
pessoa = {}
pessoa['nome'] = str(input('Digite o seu nome '))
pessoa['idade'] = int(input('Digite sua idade '))
pessoa['sexo'] = str(input('Digite seu sexo [F/M]: '))

for c,v in pessoa.items():
    print(f'{c} = {v}')

#update() ----------------------------------------------------------

d2 = {'nome':'Paulo'}
print(d2)

d2.update({'nome':'Paulo Milhomem'}) #atualiza os dados
print(d2)

d2.update({'idade':22})#inserir nova chave no dicionario
print(d2)

d2.pop('idade') #deleta o ultimo elemento do dicionário
print(d2)

d3 = {'a':10,'b':20,'c':30}
d4 = {'d':40,'e':50,'f':60}

d4.update(d3) #concatena dicionarios
print(d4)
#copy() - para fazer uma copia do dicionario ---------------

original = {'a':10,'b':20,'c':30}
copia = original.copy()

print(original)
print(copia)

copia['d'] = 40
print(copia)

#Criar uma lista vazia para armazenar o dicionário-------------------------

lista = []

q = int(input('Quantas pessoas deseja cadastrar? '))
for i in range(q):
    pessoa = {
        'nome': str(input('Digite o nome da pessoa: ')),
        'idade': int(input('Digite sua idade: ')),
        'sexo': input('Digite seu sexo [F/M]: ')
    }
    lista.append(pessoa.copy())
print(lista)

#----------------------------------------------------------

estado = {}
lista = []

for i in range(3):
    estado['uf'] = input('Digite o Estado')
    estado['sigla'] = input('Digite a sigla de estado')
    lista.append(estado.copy())
print(lista)

#Função - def nome da função()  --------------------------------

def mostra_linha():
    print('-'* 30)

mostra_linha()

def mostrar_nome(nome):
    print(f'Nome: {nome}')

mostrar_nome('THEREZA')

nome1 = input('Digite o nome 1')
nome2 = input('Digite o nome 2')
nome3 = input('Digite o nome 3')
mostrar_nome(nome1)
mostrar_nome(nome2)
mostrar_nome(nome3)
mostra_linha()

#-----------------------------------------------------------
q = int(input('Quantas pessoas deseja cadastrar? '))
for i in range(q):
    nome = input('Digite o nome da pessoa: ')
mostrar_nome(nome)
mostra_linha()

#------------------------------------------------------

def soma(a,b):
    s = a + b
    print(s)

soma(10,20)
mostra_linha()

def subtrair(a,b):
    return a - b

a = int(input('Digite o valor de a '))
b = int(input('Digite o valor de b '))
print(subtrair(a,b))
mostra_linha()

#calcular o imc de uma pessoa --------------------------------

def calculo_imc(peso,altura):
    print(peso/altura ** 2)

p = float(input('Digite o peso '))
a = float(input('Digite altura '))

calculo_imc(p,a)

#função de retorno multiplo ------------------------------------

def soma_media(a,b):
    soma = a + b
    media = (soma/2)
    return soma,media
print(soma_media(a,b))

#funçãp com apenas 1 linha -----------------------------------

def multiplicação(a,b):return a * b

a = int(input('Digite o valor de a '))
b = int(input('Digite o valor de b '))
print(multiplicação(a,b))'''

# *args -----------------------------------------------------
'''
def somar(*args):
    total = 0
    for n in args:
        total += n
    return total
print(somar(1,2,3,4,5,6,7,8,9,10))

#------------------------------------------------------------
def maior_30(*args):
    print(args)

    for n in args:
        if n > 30:
            print(n)
maior_30(10,20,30,40,50,60,70,80,90)

#------------------------------------------------------------

r = {'max':10,'meio':5,'min':0}
def funcao(*args):
    for valor in args:
        print(valor)
funcao(*r)

# **kwargs - -------------------------------------------------

def exemplo(**kwargs):
    print(kwargs)

exemplo(a=1,b=2,c=3)

#-------------------------------------------------------------

def imprimir_info_pessoa(nome,idade):
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')

info_pessoa={
    'nome':'Paulo',
    'idade':28
}
imprimir_info_pessoa(**info_pessoa)

#------------------------------------------------------------------
r = {'max':10,'meio':5,'min':0}
extra = {'passo':2}

jucao_dic={**r,**extra}
print(jucao_dic)