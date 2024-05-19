from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Registro")
root.geometry("250x250")

def enviar_datos():
    nombre = txt_nombre.get()
    
    print(f"Nombre: {nombre}")

content = ttk.Frame(root, padding = 15)
lbl_nombre = ttk.Label(content, text = "Nombre: ").grid()
txt_nombre = ttk.Entry(content, ).grid()
btn_nombre = ttk.Button(content, text = "Enviar", command=enviar_datos).grid()

content.grid()
root.mainloop()