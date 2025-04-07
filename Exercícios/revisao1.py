# 1. Escreva uma função verificar_numero que recebe um número inserido pelo
# usuário como parâmetro e imprime em uma caixa de mensagem do Tkinter
# se o número é positivo ou negativo.


# def verificar_numero():
#     try:
#         numero = float(entry_numero.get())
        
#         if numero > 0:
#             messagebox.showinfo("Resultado:", f"O número {numero:.1f} é positivo.")
#         elif numero < 0:
#             messagebox.showinfo("Resultado:", f"O número {numero:.1f} é negativo.")
#         else:
#             messagebox.showinfo("Resultado", "Zero não é positivo nem negativo.")
            
#     except ValueError:
#         messagebox.showerror("Erro", "O valor digitado é inválido")
#     finally:
#         messagebox.showinfo("Final do programa", "Obrigado por utilizar o programa.")
#         raise SystemExit
    
# root = tk.Tk()
# root.title("Verificador de Números")

# label = tk.Label(root, text="Digite um número para verificar se é positivo ou negativo:")
# label.pack(pady=10)

# entry_numero = tk.Entry(root)
# entry_numero.pack(pady=5)

# button = tk.Button(root, text="Verificar", command=verificar_numero)
# button.pack(pady=10)

# root.mainloop()


# Questão 10 (2,0 pontos): Desenvolver uma aplicação em Python utilizando Tkinter para criar uma interface
# gráfica que receba um dicionário, onde as chaves são nomes de produtos e os valores são os preços
# correspondentes. A função deve:
# ● Solicitar que o usuário insira o nome de um produto.
# ● Se o produto estiver no dicionário, exibir o preço.
# ● Se não estiver, permitir que o usuário insira o preço e adicionar o novo produto ao dicionário.
# ● O programa deve continuar até que o usuário digite "sair".
import tkinter as tk

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