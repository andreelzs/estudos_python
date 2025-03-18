# 1. Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
# teclado(entre 0 e 20) e mostrá-la por extenso. --------------------------------------------

# numeros_extenso = (
#     "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
#     "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
#     "dezoito", "dezenove", "vinte"
# )
#
# numero = int(input("Digite um número entre 0 e 20: "))
#
# if numero >= 0 and numero <= 20:
#     print(f"Você digitou o número {numeros_extenso[numero]}.")
# else:
#     print("Número fora do intervalo permitido.")



# 2. Faça um programa que preencha por leitura uma lista de 10 posições, e conta
# quantos valores diferentes existem na lista.-------------------------------

# numeros = []
# for i in range(10):
#     num = int(input(f"Digite o {i+1}º número: "))
#     numeros.append(num)
#
# valores_unicos = []
#
# for num in numeros:
#     if num not in valores_unicos:
#         valores_unicos.append(num)
#
# print(f"Existem {len(valores_unicos)} valores diferentes na lista.")



# 3.Crie um programa que leia quatro valores pelo teclado e guarde-os em uma lista.
# No final mostre:
# a)Quantas vezes apareceu o valor 9.
# b)Em que posição foi digitado o primeiro valor 3.
# c)Quais foram os números pares. ------------------------------------------

# valores = []
# digitou9 = []
# numerosPares = []
# for i in range(4) :
#     num = int(input(f"Digite o {i+1}º valor: "))
#     valores.append(num)
#     if num == 9:
#         digitou9.append(num)
#     if num % 2 == 0:
#         numerosPares.append(num)
#
# print(f"O valor 9 apareceu {len(digitou9)} vezes.")
# if 3 in valores:
#     print(f"A posição do primeiro valor 3 foi {valores.index(3)}")
# else:
#     print("O valor 3 não foi digitado.")
# print(f"Os valores pares digitados foram {numerosPares}")



# 4. Um dado é lançado 50 vezes, e o valor correspondente é armazenado em uma
# lista. Faça um programa que determine o percentual de ocorrências de face 6 do
# dado dentre esses 50 lançamentos. ------------------------------------------------------
#
# import random
# lancamentos = [random.randint(1, 6) for _ in range(50)]
# ocorrenciasFace6 = lancamentos.count(6)
# percentual = (ocorrenciasFace6 / 50) * 100
#
# print(f"Lançamentos do dado: {lancamentos}")
# print(f"A face 6 apareceu {ocorrenciasFace6} vezes.")
# print(f"Percentual de ocorrências da face 6: {percentual:.2f}%")



# 6. Estoque de Produtos:
# Implemente um sistema simples de controle de estoque de produtos. O programa
# deve permitir ao usuário adicionar novos produtos ao estoque, atualizar a
# quantidade de produtos existentes e exibir o estoque atualizado. Use um dicionário
# onde as chaves são os nomes dos produtos e os valores são as quantidades
#

# Sistema simples de controle de estoque
# estoque = {}
#
# try:
#     while True:
#         print("\n=== Controle de Estoque ===")
#         print("1. Adicionar/Atualizar Produto")
#         print("2. Exibir Estoque")
#         print("3. Sair")
#         opcao = input("Escolha uma opção: ")
#
#         if opcao == "1":
#             produto = input("Digite o nome do produto: ").strip()
#             quantidade = int(input(f"Digite a quantidade para '{produto}': "))
#             estoque[produto] = estoque.get(produto, 0) + quantidade
#             print(f"Estoque de '{produto}' atualizado para {estoque[produto]} unidades.")
#
#         elif opcao == "2":
#             if estoque:
#                 print("\n=== Estoque Atual ===")
#                 for p, q in estoque.items():
#                     print(f"{p}: {q} unidade(s)")
#             else:
#                 print("O estoque está vazio.")
#
#         elif opcao == "3":
#             print("Saindo do sistema...")
#             break
#
#         else:
#             print("Opção inválida, tente novamente.")
# except KeyboardInterrupt:
#     print("\nPrograma encerrado pelo usuário.")



# 7. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
# informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
# ordem lida.
# idade = []
# altura = []
#
# for i in range(5) :
#     idade.append(input(f"Digite a idade da pessoa {i+1}: "))
#     altura.append(input(f"Digite a altura da pessoa {i+1}: "))
#
# for i in range(4, -1, -1) :
#     print(f"Pessoa {5 - i}: Idade: {idade[i]}, Altura: {altura[i]}m")



# 8. Frequência de Letras:
# Crie um programa que receba uma string como entrada e conte o número de
# ocorrências de cada letra do alfabeto (ignorando maiúsculas/minúsculas). O
# programa deve imprimir um dicionário onde as chaves são as letras do alfabeto e os
# valores são o número de vezes que cada letra ocorre na string.







# 9. Média de Notas:
# Escreva uma função em Python que receba um dicionário contendo nomes de
# alunos e suas respectivas notas em uma disciplina. A função deve calcular a média
# das notas de todos os alunos e retornar um dicionário onde a chave é "média" e o
# valor é a média calculada.
# def calculoMedia(alunos_notas) :
#     if not alunos_notas:
#         return {"Média" : 0}
#
#     soma_notas = sum(alunos_notas.values())
#     quantidade_alunos = len(alunos_notas)
#     media = soma_notas / quantidade_alunos
#
#     return (f"Média: {media:.2f}")
#
# alunos = {
#     "André": 8.5,
#     "João": 7.0,
#     "Luan": 9.0,
#     "Gláucia": 6.5
# }
#
# resultado = calculoMedia(alunos)
# print(resultado)



# 10. Contagem de Palavras:
# Escreva um programa em Python que receba uma string como entrada e conte o
# número de ocorrências de cada palavra na string. O programa deve imprimir um
# dicionário onde as chaves são as palavras e os valores são o número de vezes que
# cada palavra ocorre na string.
# def contar_palavras(string):
#     palavras = string.lower().split()
#
#     contagem = {}
#
#     # Contar ocorrências de cada palavra
#     for palavra in palavras:
#         palavra = palavra.strip(".,!?")  # Remover pontuações simples
#         contagem[palavra] = contagem.get(palavra, 0) + 1
#
#     return contagem
#
#
# string_usuario = input("Digite uma frase: ")
#
# resultado = contar_palavras(string_usuario)
# print("Contagem das palavras:", resultado)

# 11. Escreva uma função que recebe um número n como parâmetro e imprime se n é
# positivo ou negativo.
# def verificarParidade(int):
#     if numero % 2 == 0 :
#         return (f"O número {numero} é par")
#     else :
#         return(f"O número {numero} é ímpar")
#
# numero = int(input("Digite um número inteiro para verificar a paridade: "))
# print(verificarParidade(numero))



# 12. Escreva uma função para imprimir o valor absoluto de um número.
# def imprimirValorAbsoluto(numero):
#     print(abs(numero))
#
# numero = float(input("Digite um número para descobrir o seu valor absoluto: "))
# imprimirValorAbsoluto(numero)



# 13. Escreva uma função que recebe dois números (a e b) como parâmetro e retorne
# True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.
# 14. Faça um programa com uma função chamada somaImposto. A função possui
# dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
# expressa em porcentagem e custo, que é o custo de um item antes do imposto. A
# função “altera” o valor de custo para incluir o imposto sobre vendas.
# 15. Faça uma função que informe a quantidade de dígitos de um determinado
# número inteiro informado.