# Questão 1
# Escreva uma função que receba um número do usuário e divida 100 por esse número.
# Utilize exceção para tratar casos onde o número fornecido seja zero ou não seja um número
# válido (ou seja, um erro de tipo).
def dividirPor100():
    try:
        numero = int(input("Digite um número inteiro para dividir por 100: "))
        resultado = numero / 100
    except ZeroDivisionError:
        print('Erro! Não é possível dividir por zero.')
    except (ValueError, TypeError):
        print('Erro! Valor digitado não é inteiro.')
    else:
        print(f'O resultado é: {resultado}')
dividirPor100()

#-----------------------------------------------------------------------------------------
# Questão 3
# Crie uma exceção personalizada chamada ErroIdadeInvalida, que será levantada
# quando uma pessoa tentar acessar um serviço com idade menor do que 18 anos. O código
# deve lançar essa exceção se a idade for menor e tratá-la para exibir uma mensagem de
# erro específica.
class ErroIdadeInvalida(Exception):
    def __init__(self, idade, mensagem="Idade inválida. É necessário ter pelo menos 18 anos."):
        self.idade = idade
        self.mensagem = mensagem
        super().__init__(self.mensagem)

def verificarIdade():
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 18:
            raise ErroIdadeInvalida(idade)
        print("Acesso permitido. Você preenche os requisitos de idade.")
    except ValueError:
        print("Erro! A idade fornecida não é um número inteiro válido.")
    except ErroIdadeInvalida as error:
        print(f"{error.mensagem} (Idade informada: {error.idade})")

verificarIdade()
#------------------------------------------------------------------------------------------------

# Questão 4
# Escreva uma função que solicita ao usuário a entrada de uma data (no formato
# "dd/mm/yyyy"). Caso o usuário insira uma data inválida ou mal formatada, o programa deve
# lançar e tratar a exceção com uma mensagem adequada.
from datetime import datetime
def solicitarData():
    try:
        data_input = input("Digite uma data no formato dd/mm/yyyy: ")
        data_valida = datetime.strptime(data_input, "%d/%m/%Y")
        print(f"Data digitada: {data_valida.strftime('%d/%m/%Y')}")
    except ValueError:
        print("Erro. A data fornecida está mal formatada ou é inválida. Use o formato dd/mm/yyyy.")

solicitarData()
#------------------------------------------------------------------------------------------------

# Questão 5
# Escreva um programa que receba múltiplos números inteiros de um usuário até que o
# usuário insira um valor não numérico. O programa deve capturar a exceção e exibir um
# aviso, mas continuar solicitando os números válidos.
def receberNumeros():
    numeros = []
    while True:
        try:
            entrada = input("Digite um número inteiro: ")
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida! Por favor, insira apenas números inteiros.")
        except KeyboardInterrupt:
            print("\nEncerrando o programa...")
            break
        else:
            print(f"O número {numero} foi adicionado com sucesso!")
    print("\nOs números válidos digitados foram: ", numeros)

receberNumeros()
#--------------------------------------------------------------------------------

# Questão 6
# Crie uma função que receba dois números e retorne a divisão do primeiro pelo segundo.
# Utilize exceções para capturar erros de divisão por zero e de tipo de dado incorreto. A
# exceção de tipo de dado incorreto deve ser capturada primeiro.
def dividirNumeros():
    try:
        a = int(input("Digite um número inteiro para dividir pelo segundo: "))
        b = int(input("Digite o segundo número: "))

        resultado = a / b
    except (ValueError, TypeError):
        print('Erro! Valor digitado não é inteiro.')
    except ZeroDivisionError:
        print('Erro! Não é possível dividir por zero.')
    else:
        print(f'O resultado é: {resultado}')
dividirNumeros()
#----------------------------------------------------------------------------


# Questão 9
# Crie uma função que multiplique os elementos de duas listas de números, mas antes de
# fazer a multiplicação, verifique se ambas as listas têm o mesmo tamanho. Caso contrário,
# lance uma exceção personalizada chamada ListasDeTamanhosDiferentes.
class ListasTamanhosDiferentes(Exception):
    def __init__(self, mensagem="As listas têm tamanhos diferentes."):
        super().__init__(mensagem)


def multiplicarListas(lista1, lista2):
    if len(lista1) != len(lista2):
        raise ListasTamanhosDiferentes()

    resultado = []
    for i in range(len(lista1)):
        resultado.append(lista1[i] * lista2[i])

    return resultado

try:
    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    resultado = multiplicarListas(lista_a, lista_b)
    print("Resultado:", resultado)
except ListasTamanhosDiferentes as e:
    print("Erro:", e)
#----------------------------------------------------------------------

# Questão 10
# Escreva um código que acesse valores em um dicionário baseado em chaves fornecidas
# pelo usuário. Utilize exceções para capturar o erro caso o usuário insira uma chave que não
# exista.
def acessarDicionario(dicionario, chave):
    try:
        valor = dicionario[chave]
        return valor
    except KeyError:
        print(f"Erro! A chave '{chave}' não existe no dicionário.")
        return None

if __name__ == "__main__":
    dicionarioExemplo = {
        "nome": "André",
        "idade": 18,
        "cidade": "Rio de Janeiro"
    }

    chaveUsuario = input("Digite a chave que deseja buscar no dicionário: ")

    valor = acessarDicionario(dicionarioExemplo, chaveUsuario)

    if valor is not None:
        print(f"Valor encontrado: {valor}")
    else:
        print("Chave não encontrada no dicionário.")

