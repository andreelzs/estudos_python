#Operadores aritméticos +, - , * , / , % , // , ** -----------

a,b,c,d = 2,4,6,8

s = a + b + c + d
sub = c- b
mult = a * b * c
div = a / b
mod = a % b   #resto da divisão
i = a // b    #inteiro da divisão
pot = a**b    # potência

print('A soma de {} + {} = {}'.format(a,b,s))
print(f'A soma de {a} + {b} = {s}')

print(f'A subtração de {c} - {a} = {c - a}')

print('A multiplção dos valores = {}'.format(mult))

print(f'O inteiro da divisão = {i}')

print('O numero elevado = ',pot)
print('O numero {} elevado {} = {}'.format(a,b,pot))
print(f'O numero {a} elevado {b} = {pot}')

#operadores combinados ------------------------------------

result = (5 + 3) * 2 ** 3 / 4
print(f'O resultado = {result:.0f}')

#recebendo valores externos -------------------------------

x = int(input('Digite o valor de x '))
y = float(input('Digite o valor de y '))

print(f'A divisão {x} / {y} = {x / y}')

#outra forma de converter o input para um valor numerico

x1 = input('Digite o valor de x1 ')
x2 = input('Digite o valor de x2 ')

x1 = int(x1)
x2 = float(x2)

print(f'A divisão {x1} / {x2} = {x1 / x2}')

#No python não temos incremento/decremento podemos usar += e -=

contador = 0
contador += 1

print(contador)

contador -= 2
print(contador)

#operadores relacionais >,< , <= ,<=, ==, !=

a , b = 10,20

print(a == b)
print(a != b)
print(a > b)

#Comparações encadeadas -----------------------------------

nota = 8
print(7 <= nota <= 10)

#Operadores lógicos and, or , not -------------------------

idade = 18
possui_cnh = True

print(idade >= 18 and possui_cnh)

c = 5
d = 10
print(c > 2 and d < 15 )
print(c > 2 or d > 15 )
print(c > 5 or d < 10 )

print(not possui_cnh)

#operador de associação in , not in ------------------------

n1 = [1,2,3,4,5,6,7]
print(4 in n1)
print(20 in n1)
print(20 not in n1)

#importar modulos ------------------------------------------

import math

#pow() - potencia ---------------------------------------

n1 = int(input('Digite o valor da base '))
n2 = int(input('Digite o valor da potencia '))
#n3 = math.pow(n1,n2)

print(f'O nmuero {n1} elevado {n2} = {math.pow(n1,n2)}')

#sqrt() - raiz quadrada ---------------------------------

s = math.sqrt(n1)
print(f'a raiz quadrada {n1} = {math.sqrt(n1)}')

#Arredondar  - ceil ,floor , round -------------------

print(f'A raiz quadrada {n2} = {round(s,2)}')
print(f'A raiz quadrada {s} = {math.ceil(s)}')
print(f'A raiz quadrada {s} = {math.floor(s)}')

#trunc - parte inteira do numero ----------------------

x3 = float(input('Digite o valor de x3 '))
print(f'a parte inteira do numero {x3} = {math.trunc(x3)}')

#outra forma de importar o mdulo ----------------------

from math import pow,sqrt

n3 = int(input('Digite o valor da base '))
n4 = int(input('Digite o valor da potencia '))

print(f'O numero {n3} elevado {n4} = {pow(n3,n4)}')

# random (numeros aleatorios) --------------------------

import random

#random() - numeros aleatorios entre 0 e 1 ------------------------

r = random.random()
print(f'{r:.1f}')

print(random.random() * 10)

from random import randint,randrange,uniform,choice,shuffle

print(randint(1,10)) # numeros aleatorio inteiro

print(randrange(0,20,2))#numero aleatorio com intervalo

print(uniform(5,10))#numero aleatorio flutuante definindo intervalo

i = int(input('Digite o valor inicial '))
f = int(input('Digite o valor final '))

print(randint(i,f))

l = [1,2,3,4,5,6,7]
print(choice(l)) #escolhe um elemento da lista de forma aleatoria

shuffle(l)
print(l)

'''Desafio: você quer simular a opção de jogar uma moeda e resultar
em cara ou coroa'''

#len() - quantidade de caracteres ------------------------------

nome = input('Digite o seu nome ')

print(f'O nome da pessoa é {nome} esse nome possui {len(nome)} caracteres.')

#upper() - letra maiuscula --------------------------------------

print(nome.upper())

#lower() - letra minuscula -------------------------------------

print(nome.lower())

#swapcase() - inverte a string maiusculo/minusculo e vice versa

print(nome.swapcase())

#find() - mostra a posição de um determinado elemento --------

v = 'Hoje tá osso!'
print(f'A posição da palavra osso é: {v.find('osso')}')

#replace() - alterar a string sem alterar a string principal

n = 'Maria'
print(f'O novo nome é {n.replace('Maria','Ana')}')

#count() - mostra a quantidade de vezes que determinado elemento repete

x = 'Programação'
print(f'A quantidade de vezes que a letra a repete é {x.count("a")}')

#split() - dividir string -------------------------------------
z = '      Bom dia!     '
print(z.split())

#join() - concatena uma sequencia escolhendo o separador -------

print('-'.join(z.split()))
print(' '.join(z.split()))
print('*'.join(z.split()))

#strip() - remove os espaço inicial e final -----------------

print(z)
print(z.strip())

#lstrip() - remove o espaço da esquerda ------------------

print(z.lstrip())

#rstrip() - remove o espaço da direita ------------------

print(z.rstrip())