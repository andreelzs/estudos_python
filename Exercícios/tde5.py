# Questão 1
# Escreva uma função que receba um número do usuário e divida 100 por esse número.
# Utilize exceção para tratar casos onde o número fornecido seja zero ou não seja um número
# válido (ou seja, um erro de tipo).
try:
    n = int(input('Digite um numero: '))
    print(n)
except:
    print('Erro!Digite um numero inteiro')















# Questão 2
# Crie uma função que abra um arquivo e leia seu conteúdo. Caso o arquivo não exista, exiba
# uma mensagem de erro específica. Caso ocorra outro tipo de erro, exiba uma mensagem
# genérica.
# Questão 3
# Crie uma exceção personalizada chamada ErroIdadeInvalida, que será levantada
# quando uma pessoa tentar acessar um serviço com idade menor do que 18 anos. O código
# deve lançar essa exceção se a idade for menor e tratá-la para exibir uma mensagem de
# erro específica.
# Questão 4
# Escreva uma função que solicita ao usuário a entrada de uma data (no formato
# "dd/mm/yyyy"). Caso o usuário insira uma data inválida ou mal formatada, o programa deve
# lançar e tratar a exceção com uma mensagem adequada.
# Questão 5
# Escreva um programa que receba múltiplos números inteiros de um usuário até que o
# usuário insira um valor não numérico. O programa deve capturar a exceção e exibir um
# aviso, mas continuar solicitando os números válidos.
# Questão 6
# Crie uma função que receba dois números e retorne a divisão do primeiro pelo segundo.
# Utilize exceções para capturar erros de divisão por zero e de tipo de dado incorreto. A
# exceção de tipo de dado incorreto deve ser capturada primeiro.
# Questão 7
# Escreva uma função recursiva que pede um número inteiro e calcula o fatorial. Caso o
# número não seja válido (não seja um inteiro positivo), deve-se lançar uma exceção
# personalizada ValorNaoPositivo.
#
# Questão 8
# Crie uma função que valide um número de telefone. O número de telefone deve ser
# verificado quanto ao seu formato e a exceção deve ser lançada se o formato não for válido
# (exemplo: "123-456-7890"). Utilize exceções para indicar que o número é inválido.
# Questão 9
# Crie uma função que multiplique os elementos de duas listas de números, mas antes de
# fazer a multiplicação, verifique se ambas as listas têm o mesmo tamanho. Caso contrário,
# lance uma exceção personalizada chamada ListasDeTamanhosDiferentes.
# Questão 10
# Escreva um código que acesse valores em um dicionário baseado em chaves fornecidas
# pelo usuário. Utilize exceções para capturar o erro caso o usuário insira uma chave que não
# exista.