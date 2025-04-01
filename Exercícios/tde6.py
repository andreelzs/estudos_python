import tkinter as tk
from tkinter import messagebox

#1--------------------------------------------------------------------------------------------
def verificar_numero():
    entrada = entrada_numero.get()

    try:
        numero = float(entrada)

        if numero > 0:
            resultado = "Positivo!"
        elif numero < 0:
            resultado = "Negativo!"
        else:
            resultado = "Zero!"

        messagebox.showinfo("Resultado", f"O valor digitado: {numero} é {resultado}")

    except ValueError:
        messagebox.showerror("Erro", "O valor digitado é inválido")


janela = tk.Tk()
janela.title("Verificador de Números")

tk.Label(janela, text="Digite um número:").grid(row=0, column=0, padx=10, pady=5)
entrada_numero = tk.Entry(janela)
entrada_numero.grid(row=0, column=1, padx=10, pady=5)

tk.Button(
    janela,
    text = "Verificar",
    command = verificar_numero
).grid(row=1, column=0, columnspan=2, pady=10)

janela.mainloop()


#2---------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

def verificar_bissexto():
    try:
        ano = int(entrada_ano.get())
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        messagebox.showinfo("Resultado", f"O ano {ano} é bissexto!" if bissexto else f"O ano: {ano} não é bissexto!")
    except:
        messagebox.showerror("Erro", "Ano inválido!")

janela = tk.Tk()
janela.title("Verificador Ano Bissexto")

tk.Label(janela, text="Digite o ano:").grid(row=0, column=0, padx=10, pady=5)
entrada_ano = tk.Entry(janela)
entrada_ano.grid(row=0, column=1, padx=10, pady=5)

tk.Button(
    janela,
    text="Verificar",
    command=verificar_bissexto
).grid(row=1, column=0, columnspan=2, pady=10)

janela.mainloop()


#3----------------------------------------------------------------------------------------------------------
import tkinter as tk


def calcular_operacoes():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())

        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2

        divisao = num1 / num2 if num2 != 0 else "não é possível dividir por zero."

        resultados = (
            f"Soma: {soma}\n"
            f"Subtração: {subtracao}\n"
            f"Multiplicação: {multiplicacao}\n"
            f"Divisão: {divisao}"
        )

    except ValueError:
        resultados = "Erro: Digite números válidos!"

    label_resultados.config(text=resultados)


janela = tk.Tk()
janela.title("Calculadora")

tk.Label(janela, text="Primeiro número:").grid(row=0, column=0, padx=10, pady=5)
entrada_num1 = tk.Entry(janela)
entrada_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Segundo número:").grid(row=1, column=0, padx=10, pady=5)
entrada_num2 = tk.Entry(janela)
entrada_num2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(
    janela,
    text="Calcular",
    command=calcular_operacoes
).grid(row=2, column=0, columnspan=2, pady=10)

label_resultados = tk.Label()
label_resultados.grid(row=3, column=0, columnspan=2)

janela.mainloop()

#4--------------------------------------------------------------------------------------------
import tkinter as tk


def processar_numeros():
    try:
        numeros = [
            int(entrada1.get()),
            int(entrada2.get()),
            int(entrada3.get()),
            int(entrada4.get())
        ]

        qtd_9 = numeros.count(9)
        pos_3 = numeros.index(3) if 3 in numeros else -1
        pares = [num for num in numeros if num % 2 == 0]

        resultado = (
            f"a) Quantidade de números 9: {qtd_9}\n"
            f"b) Primeiro 3 na posição: {pos_3}\n"
            f"c) Números pares: {', '.join(map(str, pares)) if pares else 'Nenhum'}"
        )

    except ValueError:
        resultado = "Digite números inteiros válidos!"

    label_resultados.config(text=resultado)


janela = tk.Tk()
janela.title("Analisar Números")

tk.Label(janela, text="Digite 4 números:").grid(row=0, column=0, columnspan=4, pady=5)

entrada1 = tk.Entry(janela, width=5)
entrada1.grid(row=1, column=0, padx=5)
entrada2 = tk.Entry(janela, width=5)
entrada2.grid(row=1, column=1, padx=5)
entrada3 = tk.Entry(janela, width=5)
entrada3.grid(row=1, column=2, padx=5)
entrada4 = tk.Entry(janela, width=5)
entrada4.grid(row=1, column=3, padx=5)

tk.Button(
    janela,
    text="Analisar",
    command=processar_numeros
).grid(row=2, column=0, columnspan=4, pady=10)

label_resultados = tk.Label(janela, text="")
label_resultados.grid(row=3, column=0, columnspan=4)

janela.mainloop()