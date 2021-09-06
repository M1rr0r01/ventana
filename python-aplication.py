from tkinter import *
from tkinter.ttk import *

veni=Tk()
veni.title("Inicio de sesión")
veni.geometry("300x200")
veni.resizable(width=False, height=False)

luser=Label(veni, text="Usuario")
luser.pack()

user=StringVar()
tuser=Entry(veni, width=30, textvariable=user)
tuser.pack()

lpas=Label(veni, text="Contraseña")
lpas.pack()

pas=StringVar()
tpas=Entry(veni, width=30, textvariable=pas, show="*")
tpas.pack()

def ingresar():
    if user.get()=="jes" and pas.get()=="jes":
         veni.destroy()
         veni2=Tk()
         veni2.title("Bienvenido")
         veni2.geometry("200x150")
                       
    else:
         veni.title("Incorrecto")

def cerrar():
    veni.destroy()
    print("Gracias por usar este sistema")

b1=Button(veni, text="Ingresar", command=ingresar)
b1.pack(side=LEFT)

b2=Button(veni, text="Cerrar", command=cerrar)
b2.pack(side=RIGHT)

veni.mainloop()
