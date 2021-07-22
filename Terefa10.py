# Luísa Gonçalves Ferreira

from tkinter import *
import tkinter as tk

janela=Tk()
janela.title("Tarefa 10 de Instrumentação II(Luísa)")
janela.geometry('750x350')
janela.configure(bg='magenta',background='pink')

faixa1=Label(janela,text="______________________________________________________________",foreground='cyan',background='pink')
faixa1.configure(font=(50))
faixa1.pack()

texto1=Label(janela,text="Implementando uma interface com o usuário(IU):",pady=25,background='pink')
texto1.pack()
texto1.configure(font=("Microsoft JhengHei UI", 20))

texto2=Label(janela, text="Biblioteca em Python utilizada: Tkinter.",relief=SOLID,background='cyan')
texto2.pack()

texto3=Label(janela,text="Observação: Serão utilizados widgets para mudar as características da IU.",pady=15,background='pink')
texto3.configure(font=("Arial", 12, "italic"))
texto3.pack()

texto4=Label(janela,text="Dessa forma, as frases foram configuradas apresentando distintas características.",background='pink')
texto4.configure(font=("Nirmala UI", 15))
texto4.pack()

texto4=Label(janela,text="Para fechar a janela, clique no botão abaixo.",foreground='magenta',pady=20,background='pink')
texto4.configure(font=("Arial", 15, "italic"))
texto4.pack()

def close_window():
    janela.destroy()

botao = tk.Button(text = "Fechar janela", command = close_window,relief=SUNKEN,cursor="heart")
botao.pack()

faixa2=Label(janela,text="______________________________________________________________",foreground='cyan',background='pink')
faixa2.configure(font=(50))
faixa2.pack()

janela.mainloop()