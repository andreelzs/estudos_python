import tkinter as tk
from tkinter import messagebox

# 1. Escreva uma função verificar_numero que recebe um número inserido pelo
# usuário como parâmetro e imprime em uma caixa de mensagem do Tkinter
# se o número é positivo ou negativo.
def verificar_numero():
    try:
        numero = float(entry_numero.get())
        
        if numero > 0:
            messagebox.showinfo("Resultado:", f"O número {numero:.1f} é positivo.")
        elif numero < 0:
            messagebox.showinfo("Resultado:", f"O número {numero:.1f} é negativo.")
        else:
            messagebox.showinfo("Resultado", "Zero não é positivo nem negativo.")
            
    except ValueError:
        messagebox.showerror("Erro", "O valor digitado é inválido")
    finally:
        messagebox.showinfo("Final do programa", "Obrigado por utilizar o programa.")
        raise SystemExit
    
root = tk.Tk()
root.title("Verificador de Números")

label = tk.Label(root, text="Digite um número para verificar se é positivo ou negativo:")
label.pack(pady=10)

entry_numero = tk.Entry(root)
entry_numero.pack(pady=5)

button = tk.Button(root, text="Verificar", command=verificar_numero)
button.pack(pady=10)

root.mainloop()


# Questão 10 (2,0 pontos): Desenvolver uma aplicação em Python utilizando Tkinter para criar uma interface
# gráfica que receba um dicionário, onde as chaves são nomes de produtos e os valores são os preços
# correspondentes. A função deve:
# ● Solicitar que o usuário insira o nome de um produto.
# ● Se o produto estiver no dicionário, exibir o preço.
# ● Se não estiver, permitir que o usuário insira o preço e adicionar o novo produto ao dicionário.
# ● O programa deve continuar até que o usuário digite "sair".
# import tkinter as tk

root = tk.Tk()
root.title("Preços de Produtos")
root.geometry("300x250")

produtos = {}

label_nome = tk.Label(root, text="Nome do Produto:")
label_nome.grid(row=0, column=0, padx=10, pady=10)

entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_preco = tk.Label(root, text="Preço do Produto:")
label_preco.grid(row=1, column=0, padx=10, pady=10)

entry_preco = tk.Entry(root)
entry_preco.grid(row=1, column=1, padx=10, pady=10)

def buscar_preco():
    nome = entry_nome.get()
    if nome in produtos:
        preco = produtos[nome]
        label_resultado.config(text=f"Preço: R${preco:.2f}")
    else:
        label_resultado.config(text="Produto não encontrado")

def adicionar_produto():
    nome = entry_nome.get()
    preco = float(entry_preco.get())
    produtos[nome] = preco
    label_resultado.config(text=f"Produto adicionado com sucesso!")

button_buscar = tk.Button(root, text="Buscar", command=buscar_preco)
button_buscar.grid(row=2, column=0, columnspan=2, pady=10)

button_adicionar = tk.Button(root, text="Adicionar", command=adicionar_produto)
button_adicionar.grid(row=3, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(root, text="")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()


# 1. Escreva uma função verificar_numero que recebe um número inserido pelo
# usuário como parâmetro e imprime em uma caixa de mensagem do Tkinter
# se o número é positivo ou negativo.

def verificar_numero():
    try:
        numero = float(entry_numero.get())

        if numero > 0:
            messagebox.showinfo("Resultado", f"O número {numero:.1f} é positivo.")
        elif numero < 0:
            messagebox.showinfo("Resultado", f"O número {numero:.1f} é negativo.")
        elif numero == 0:   
            messagebox.showinfo("Resultado", "Zero não é positivo nem negativo.")
    
    except ValueError or TypeError:
        messagebox.showerror("Erro", "O valor digitado é inválido")

root = tk.Tk()
root.title("Verificador de Números")

label = tk.Label(root, text="Digite um número para verificar se é positivo ou negativo:")
label.pack(pady=10)

entry_numero = tk.Entry(root)
entry_numero.pack(pady=5)

button = tk.Button(root, text="Verificar", command=verificar_numero)
button.pack(pady=10)

root.mainloop()


# 2. Criar uma interface Tkinter que permita ao usuário inserir uma lista ordenada
# de números e um limite desejado. Em seguida, ao pressionar um botão, a
# função verificará se há algum elemento na lista maior que o limite desejado e
# retornará o índice do primeiro elemento que atenda a essa condição, ou
# retornará -1 se nenhum elemento for maior que o limite desejado.
import tkinter as tk

def verificar_limite():
    # Recupera os dados da interface
    lista_texto = entry_lista.get()
    limite_texto = entry_limite.get()

    # Validação: verifica se a entrada do limite é um número
    try:
        limite = float(limite_texto)
    except ValueError:
        resultado_label.config(text="Erro: Digite um número válido para o limite!")
        return

    # Converte a string com números separados por vírgula em uma lista de float
    try:
        # Remove espaços e converte cada número
        lista_numeros = [float(num.strip()) for num in lista_texto.split(",") if num.strip() != ""]
    except ValueError:
        resultado_label.config(text="Erro: Certifique-se de digitar números separados por vírgula.")
        return

    # Verifica se há algum elemento na lista maior que o limite
    indice_encontrado = -1
    for index, num in enumerate(lista_numeros):
        if num > limite:
            indice_encontrado = index
            break

    # Exibe o resultado
    resultado_label.config(text=f"Índice do primeiro elemento maior que {limite}: {indice_encontrado}")

# Configuração da janela principal
root = tk.Tk()
root.title("Verificação de Limite")
root.geometry("500x300")

# Rótulo e entrada para a lista de números
label_lista = tk.Label(root, text="Digite uma lista ordenada de números (separados por vírgula):", font=("Arial", 12))
label_lista.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

entry_lista = tk.Entry(root, font=("Arial", 12), width=40)
entry_lista.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Rótulo e entrada para o limite desejado
label_limite = tk.Label(root, text="Digite o limite desejado:", font=("Arial", 12))
label_limite.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_limite = tk.Entry(root, font=("Arial", 12))
entry_limite.grid(row=2, column=1, padx=10, pady=10)

# Botão para executar a verificação
botao_verificar = tk.Button(root, text="Verificar", font=("Arial", 12), command=verificar_limite)
botao_verificar.grid(row=3, column=0, columnspan=2, pady=20)

# Label para exibir o resultado
resultado_label = tk.Label(root, text="", font=("Arial", 12))
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Inicia o loop da interface gráfica
root.mainloop()


# 3. Criar uma interface Tkinter que permita ao usuário inserir um ano e, ao
# pressionar um botão, a função verificará se o ano é bissexto ou não. Em
# seguida, exibirá uma mensagem indicando o resultado.

def verificar_ano():
    try:
        ano = int(entry_ano.get())
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        messagebox.showinfo("Resultado", f"O ano {ano} é bissexto!" if bissexto else f"O ano: {ano} não é bissexto!")
    except (ValueError, TypeError):
        messagebox.showerror("Erro", "Ano inválido!")

root = tk.Tk()
root.geometry("300x200")
root.title("Verificador de Ano Bissexto")

label_ano = tk.Label(root, text="Digite um ano: ")
label_ano.pack(pady=10)

entry_ano = tk.Entry(root)
entry_ano.pack(pady=10)
 
button= tk.Button(root, text= "Verificar", command=verificar_ano)
button.pack(pady=10)

root.mainloop()


# 4. Criar uma calculadora básica em Tkinter que permita ao usuário inserir dois
# números e, ao pressionar um botão, exibirá o resultado da
# adição,subtração,multiplicação e divisão desses dois números.

def calcular():

    try: 
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        divisao = num1 / num2 if num2 != 0 else "Indefinido"
        
        messagebox.showinfo("Resultado", f"Soma: {soma:.1f}\nSubtração: {subtracao:.1f}\nMultiplicação: {multiplicacao:.1f}\nDivisão: {divisao:.1f}")

    except ZeroDivisionError:
        messagebox.showerror("Erro", "Não é possível dividir por zero.")
    except (ValueError, TypeError):
        messagebox.showerror("Erro", "Os valores digitados é inválido.")
        
root = tk.Tk()
root.title("Calculadora Básica")
root.geometry("300x200")

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(root, text="Digite dois números para fazer os cálculos: ")
label.pack(pady=10)

entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(frame)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(frame, text="Calcular", command=calcular)
button.grid(row=1, columnspan=2, pady=10)

root.mainloop()


# 5. Criar uma interface Tkinter que permita ler quatro valores pelo teclado e
# guarde-os em uma lista.
# No final mostre:
# a)Quantas vezes apareceu o valor 9.
# b)Em que posição foi digitado o primeiro valor 3.
# c)Quais foram os números pares. enunciado para tkinter

import tkinter as tk

def processar_valores():
    try:
        # Coleta e converte os valores dos Entry para inteiros
        valor1 = int(entry1.get())
        valor2 = int(entry2.get())
        valor3 = int(entry3.get())
        valor4 = int(entry4.get())
    except ValueError:
        resultado_label.config(text="Erro: por favor, digite apenas números inteiros!")
        return

    # Armazena os valores em uma lista
    lista_valores = [valor1, valor2, valor3, valor4]

    # a) Quantas vezes apareceu o valor 9.
    vezes_nove = lista_valores.count(9)

    # b) Em que posição foi digitado o primeiro valor 3.
    try:
        posicao_tres = lista_valores.index(3)
        posicao_msg = f"{posicao_tres} (posição índice, iniciando em 0)"
    except ValueError:
        posicao_msg = "Não foi digitado o valor 3."

    # c) Quais foram os números pares.
    pares = [str(num) for num in lista_valores if num % 2 == 0]
    msg_pares = ", ".join(pares) if pares else "Nenhum número par encontrado"

    # Monta a mensagem de resultado
    mensagem = (
        f"Lista de valores: {lista_valores}\n"
        f"Valor 9 apareceu {vezes_nove} vezes\n"
        f"Primeiro valor 3 está na: {posicao_msg}\n"
        f"Números pares: {msg_pares}"
    )

    resultado_label.config(text=mensagem)

# Criando a janela principal
root = tk.Tk()
root.title("Leitura de 4 Valores")
root.geometry("400x300")

# Rótulo de instrução
label_instrucao = tk.Label(root, text="Digite quatro valores:", font=("Arial", 12))
label_instrucao.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entrada para o valor 1
label1 = tk.Label(root, text="Valor 1:", font=("Arial", 12))
label1.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.grid(row=1, column=1, padx=10, pady=5)

# Entrada para o valor 2
label2 = tk.Label(root, text="Valor 2:", font=("Arial", 12))
label2.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.grid(row=2, column=1, padx=10, pady=5)

# Entrada para o valor 3
label3 = tk.Label(root, text="Valor 3:", font=("Arial", 12))
label3.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry3 = tk.Entry(root, font=("Arial", 12))
entry3.grid(row=3, column=1, padx=10, pady=5)

# Entrada para o valor 4
label4 = tk.Label(root, text="Valor 4:", font=("Arial", 12))
label4.grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry4 = tk.Entry(root, font=("Arial", 12))
entry4.grid(row=4, column=1, padx=10, pady=5)

# Botão para processar os valores digitados
btn_processar = tk.Button(root, text="Processar Valores", font=("Arial", 12), command=processar_valores)
btn_processar.grid(row=5, column=0, columnspan=2, pady=20)

# Label para exibir os resultados
resultado_label = tk.Label(root, text="", font=("Arial", 12))
resultado_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
