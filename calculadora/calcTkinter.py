import tkinter as tk

def adicionar_numero(num):
    campo_texto.insert(tk.END, num)

def calcular():
    expressao = campo_texto.get()
    resultado = eval(expressao)
    campo_texto.delete(0, tk.END)
    campo_texto.insert(tk.END, resultado)

def apagar():
    campo_texto.delete(0, tk.END)

janela = tk.Tk()

campo_texto = tk.Entry(janela, width=20)
campo_texto.grid(row=0, column=0, columnspan=4)

botoes = [
    "1", "2", "3", "/",
    "4", "5", "6", "*",
    "7", "8", "9", "-",
    "0", ".", "", "+"
]

row = 1
col = 0
for botao in botoes:
    tk.Button(janela, text=botao, width=5, command=lambda num=botao: adicionar_numero(num)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(janela, text="Calcular", width=10, command=calcular).grid(row=row, column= 0, columnspan=2)
tk.Button(janela, text="C", width=10, command=apagar).grid(row=row, column=2, columnspan=2)

janela.mainloop()