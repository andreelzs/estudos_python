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
from tkinter import simpledialog, messagebox

def main():
    # Dicionário de produtos
    produtos = {}
    
    # Configuração da janela principal
    root = tk.Tk()
    root.title("Gerenciador de Produtos")
    root.geometry("400x200")
    
    # Função principal de processamento
    def verificar_produto():
        nome = entrada.get().strip()
        entrada.delete(0, tk.END)
        
        if not nome:
            messagebox.showwarning("Aviso", "Digite um produto válido!")
            return
            
        if nome.lower() == "sair":
            root.destroy()
            return
            
        if nome in produtos:
            messagebox.showinfo("Resultado", f"Preço de {nome}: R${produtos[nome]:.2f}")
        else:
            preco = simpledialog.askfloat("Novo Produto", f"Digite o preço para {nome}:")
            if preco is not None:  # Se usuário não cancelar
                produtos[nome] = preco
                messagebox.showinfo("Sucesso", f"{nome} adicionado com sucesso!")
    
    # Elementos da interface
    tk.Label(root, text="Digite o nome do produto:", font=("Arial", 12)).pack(pady=10)
    
    entrada = tk.Entry(root, width=30, font=("Arial", 12))
    entrada.pack(pady=5)
    entrada.focus()
    
    tk.Button(
        root, 
        text="Verificar/Adicionar", 
        command=verificar_produto,
        font=("Arial", 12),
        bg="#4CAF50",
        fg="white"
    ).pack(pady=10)
    
    root.mainloop()
