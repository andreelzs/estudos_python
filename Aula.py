import tkinter as tk

def enviar():
    print(f"Nome: {entry_nome.get()}")
    print(f"Idade: {scale_idade.get()}")
    print(f"Curso: {var_radio.get()}")
    print(f"Termos aceitos: {var_check.get()}")

root = tk.Tk()
root.title("Formulário")

# Widgets
tk.Label(root, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Idade:").grid(row=1, column=0)
scale_idade = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale_idade.grid(row=1, column=1)

var_radio = tk.StringVar(value="Python")
tk.Label(root, text="Curso:").grid(row=2, column=0)
tk.Radiobutton(root, text="Python", variable=var_radio, value="Python").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Java", variable=var_radio, value="Java").grid(row=3, column=1, sticky="w")

var_check = tk.BooleanVar()
tk.Checkbutton(root, text="Aceito os termos", variable=var_check).grid(row=4, columnspan=2)

tk.Button(root, text="Enviar", command=enviar).grid(row=5, columnspan=2, pady=10)

root.mainloop()