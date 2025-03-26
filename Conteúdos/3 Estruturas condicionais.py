#Estrutura condicional if/else/elif ------------------
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

if a > b:
    print(f'O valor {a} é maior que o valor  {b}')
else:
    print(f'O valor {a} não é maior que o valor {b}')

#-----------------------------------------------------
nome = input('Digite seu nome: ')
if nome == 'Gustavo':
    print(f'Oi!Seja bem vindo {nome}!')
print(f'Bom dia {nome}!')

#------------------------------------------------------
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print(f'A pessoa tem {idade} anos já pode dirigir.')
else:
    print(f'A pessoa tem {idade} anos não pode dirigir.')

#-------------------------------------------------------
c = int(input('Digite o valor de c: '))
d = int(input('Digite o valor de d: '))

res = 0
op = input('Digite a operação: +,-,*,/ ')
if op == '+':
    res = c + d
    print(f'A soma {c} + {d} = {res}')
elif op == '-':
    res = c - d
    print(f'A subtração {c} - {d} = {res}')
elif op == '*':
    res = c * d
    print(f'A multiplicação {c} * {d} = {res}')
elif op == '/':
    res = c / d
    print(f'A divisão {c} / {d} = {res}')
print('Término do calculo.')

#operador ternário ---------------------------------------------

idade = int(input('Digite sua idade: '))
print('Maior de idade' if idade >= 18 else 'Menor de idade')

#--------------------------------------------------------------

nota = float(input('Digite sua nota: '))
print('Aprovado' if nota >= 6 else 'Reprovado')

#-------------------------------------------------------------
numero = int(input('Digite sua numero: '))
if numero <= 10 and numero % 2 == 0:
    print(f'O valor {numero} é menor que 10 e é par')
else:
    print('Não atende a condição')

#For ----------------------------------------------------------
e = 0
f = 10
for i in range(e,f):
    print('Olá!')
#--------------------------------------------------------------
for j in range(10):
    print(j)

#--------------------------------------------------------------

for j in range(1,9):
    print(j)

#--------------------------------------------------------------

for numero in range(1,11):
    if numero % 2 == 0:
        print(f'O numero {numero} é par.')
    else:
        print(f'O numero {numero} é impar.')

#--------------------------------------------------------------
for num in range(10,40,2):
    print(f'Numero: {num}')

#-----------------------------------------------------------

for num in range(40,10,-2):
    print(f'Numero: {num}')

#-----------------------------------------------------------

for n in range(10):
    if n > 6:
        break
    print(f'Numero: {n}')
print('Fim')

#----------------------------------------------------------
for n in range(20,30):
    if n == 25:
        continue
    print(f'Numero: {n}')

#tabuada --------------------------------------------------

t = int(input('Digite o valor da tabuada desejada: '))
for tabuada in range(0,11):
    print(f'{t} x {tabuada} = {t * tabuada}')

#--------------------------------------------------------
nome = 'Thereza'
for p,v in enumerate(nome):
    print(f'{p} {v}')
#while --------------------------------------------------

n = 1
while n != 0:
    n = int(input(f'Digite o valor {n}: '))
print('Terminou')

#---------------------------------------------------------

n = 1
par = impar = 0
while n != 0:
    n = int(input(f'Digite o valor {n}: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} numeros pares e {impar} impares')

#--------------------------------------------------------------

num = 0
while num < 5:
    num += 1
    if num == 3:
        break
    print(num)
#-----------------------------------------------------------

#import random

from random import randint

c = randint(1,10)
print('Tente adivinhar o numro...')

acerto = False
while not acerto:
    j = int(input('Qual o seu palpite?: '))
    if j == c:
        acerto = True
        print('Acertou!😊')
    else:
        print('Errou!Tente novamente!🤷')

#----------------------------------------------------------

x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))

op = 0
while op != '5':
    print(
    '''[1]Somar
    [2]Subtrair
    [3]Multiplicar
    [4]Dividir
    [5]Sair''')
    op = input('Escolha a opção desejada: ')

    if op == '1':
        print(f'A soma {x} + {y} = {x + y}')
    elif op == '2':
        print(f'A subtração {x} - {y} = {x - y}')
    elif op == '3':
        print(f'A multiplicação {x} * {y} = {x * y}')
    elif op == '4':
        print(f'A divisão {x} / {y} = {x / y}')
    elif op == '5':
        print('Termino do programa!')
    else:
        print('Opção invalida!')
    print('Fim do programa!')