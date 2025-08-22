import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Relógio")
root.iconbitmap("escudo.ico")  

label = tk.Label(root, font=('Helvetica', 50), background='black', foreground='white')
label.pack(anchor='center')  # Corrigido "anvhor" para "anchor"

def relogio():
    hora = strftime('%H:%M:%S')
    label.config(text=hora)
    label.after(1000, relogio)

relogio()
root.mainloop()
