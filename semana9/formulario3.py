from tkinter import Tk,messagebox, Label, Entry, Button

root = Tk()

root.config(width=300, height=250)
root.title("Registro")

def calcular_salario(): 
    cod = txt_cod.get()
    nom = txt_nom.get()
    tar = float(txt_tar.get())
    hor = int(txt_hor.get())
    sb = tar * hor
    desc = sb * 0.12
    sn = sb - desc
    messagebox.showinfo("Reporte", f"")


lbl_cod = Label(root, text = "Ingresar código:")
txt_cod = Entry(root)
txt_cod.grid()

lbl_nom = Label(root, text = "Ingresar nombre:")
txt_nom = Entry(root)
txt_nom.grid()

lbl_tar = Label(root, txt = "Ingresar tarifa:")
txt_tar = Entry(root)
txt_tar.grid()

lbl_hor = Label(root, text = "Ingresar horas trabajadas:")
txt_hor = Entry(root)
txt_hor.grid()