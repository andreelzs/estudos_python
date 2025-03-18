#_*_coding:utf-8_*_

#comentário de 1 linha
'''comentário de multiplas linhas'''

print('Feliz 2025!Bom dia!Sejam Bem-Vindos!')

#tipos de dados - inteiro,float,string, booleano

nome = 'Thereza'
idade = 22
altura = 1.61
aprovado = True

print(nome,idade,altura,aprovado)

print(2 + 2)
#print('2' + 2)
print('2' + '2')
print('Olá',5)
#print('Olá'+ 5)
print(3,3)
print('Olá' + '' + ' 5')

#Variavel ------------------------------------------

nome = 'Thereza'
sobrenome='Gondim'

print(nome,sobrenome)

a = 1
b = 2
c = 3.9456543

print('O valor de a = ',a,'O valor de b = ',b,'O valor de c = ',round(c))

# print usando o .format() , mascara {}

print('O valor de a = {}'.format(a),'\nO valor de b = {}'.format(b),'\nO valor de c = {:.2f}'.format(c))
print('O valor de a = {} o valor de b = {} e o valor de c = {:.1f}'.format(a,b,c))

# f string ------------------------------------------------------------------

print(f'O valor de a = {a}, o valor de b = {b}, o valor de c = {c:.2f}')