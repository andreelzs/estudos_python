#Exceção :https://docs.python.org/3/library/exceptions.html

try:
    operação
except:
    falha
else:
    certo
finally:
    mostra resposta independente de certo ou errado
#------------------------------------------------------
try:
    n = int(input('Digite um numero: '))
    print(n)
except:
    print('Erro!Digite um numero inteiro')


#------------------------------------------------------
try:
    #x = int(input('Digite um numero: '))
    print(x)
except:
    print('Erro!')

try:
    x = int(input('Digite um numero: '))
    print(x)
except NameError:
    print('Erro!O valor de x não foi definido')
except:
    print('Erro! desconhecido')

#-------------------------------------------------
try:
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    r = a/b
except:
    print('Erro!tivemos um problema no sistema')
else:
    print(f'O resultado : {r}')
finally:
    print('Volte sempre')
#------------------------------------------------------
try:
    num = int(input('Digite um numero: '))
    print(num)
    10/0
except ZeroDivisionError:
    print('Erro!Divisão por zero não é possivel')
except ValueError:
    print('Erro!Digite um numero válido')
finally:
    print('Fim do programa')

try:
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    r = a/b
except(ValueError,TypeError):
    print('Erro!Tivemos um problema no sistema')
except ZeroDivisionError:
    print('Erro!Não pode dividir por zero')
except KeyboardInterrupt:
    print('Saindo do programa!O usuário preferiu não informar os dados')
else:
    print(f'O resultado : {r}')
finally:
    print('Volte sempre')

#---------------------------------------------------------------------
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print('Erro!Digite um numero inteiro')
            continue
        else:
            return num
m = leiaInt('Digite um numero inteiro: ')
print(f'O valor digitado :{m}')
#----------------------------------------------------------------------
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro!Digite um numero inteiro')
            continue
        else:
            return num

m = leiaInt('Digite um numero inteiro: ')
print(f'O valor digitado :{m}')

#Calcular a media --------------------------------------------------

#Cabeçalho da função
def calcular_media(lista):
    try:
        media = sum(lista) / len(lista)
    except ZeroDivisionError:
        print('Erro!Não pode dividir por zero')
    except ValueError:
        print('A lista contem valores incompativeis')
    else:
        print('A media foi calculada com sucesso!')
        return media
    finally:
        print('Volte sempre')

#"main"
valores = []
while True:
    valor = input('Digite um valor(ou fim para encerrar a lista): ')
    if valor.lower() == 'fim':
        break
    try:
        valores.append(float(valor))
    except (ValueError, TypeError):
        print('\033[31mErro!Digite um numero inteiro\033[m')

media = calcular_media(valores)
if media is not None:
    print(f'A media foi de: {media}')

#---------------------------------------------------------------------
def calcular_media(notas):
    try:
        media = sum(notas) / len(notas)
        if media >= 6:
            return 'Aprovado'
        else:
            return 'Reprovado'
    except ZeroDivisionError:
        print('Erro!Não pode dividir por zero')
    except ValueError:
        print('A lista contem valores incompativeis')
    else:
        print('A media foi calculada com sucesso!')
        return media
    finally:
        print('Volte sempre')

notas = []
while True:
    nota_str = input('Digite a nota(ou fim para encerrar a lista): ')
    if nota_str.lower() == 'fim':
        break
    try:
        nota = float(nota_str)
        if nota < 0 or nota >10:
            raise ValueError('A nota deve estar entre 0 e 10')
        notas.append(nota)
    except (ValueError, TypeError):
        print('\033[31mErro!Digite um numero inteiro\033[m')
resultado = calcular_media(notas)
print('Resultado',resultado)