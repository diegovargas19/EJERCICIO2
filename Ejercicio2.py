#Ejercicio2
#Vargas Gonzalez Diego Alejandro
#15 de marzo 2023

from tkinter import*
from tkinter import ttk
import tkinter as tk


raiz = Tk()
raiz.geometry("618x520")
raiz.config(bg="black")

imagen = PhotoImage(file="carrito.png")
imagen2 = PhotoImage(file="lupa.png")
imagen3 = PhotoImage(file="limpiar.png")
imagen4 = PhotoImage(file="back.png")

gris = Frame(raiz, bg="gray39", width=650, height=90)
gris.grid(column=0, row=0)

mainFrame = Frame(raiz, bg="IndianRed4",width=590, height=200)
mainFrame.grid(column=0, row=2, pady=8)

rojoint = Frame(mainFrame, bg="black", width=650, height=90)
rojoint.grid(column=0, row=1, padx=40)

rojo = Frame(rojoint, bg="IndianRed4",width=350, height=190)
rojo.grid(column=0, row=0)

rojo2 = Frame(rojoint, bg="IndianRed4",width=300, height=190)
rojo2.grid(column=1, row=0)

imagenesenrojo2 = Frame(rojo2, bg="IndianRed4")
imagenesenrojo2.grid(column=0, row=0)

tablaFrame = Frame(mainFrame, bg="IndianRed4",width=590, height=200)
tablaFrame.grid(column=0, row=2, pady=20)

abajo = Frame(mainFrame, bg="IndianRed4",width=300, height=10)
abajo.grid(column=0, row=3)









etqImagen =Label(gris, bg="gray39")
etqImagen.grid(column=0, row=0)
etqImagen['image']= imagen

botonImagen2 =Button(imagenesenrojo2, bg="gray39", borderwidth=0)
botonImagen2.grid(column=0, row=0,padx=7)
botonImagen2['image']= imagen2

botonImagen3 =Button(imagenesenrojo2, bg="gray39", borderwidth=0)
botonImagen3.grid(column=1, row=0,padx=7)
botonImagen3['image']= imagen3

botonImagen4 =Button(imagenesenrojo2, bg="gray39", borderwidth=0)
botonImagen4.grid(column=2, row=0, padx=7)
botonImagen4['image']= imagen4

etqTexto = Label(gris, bg="gray39", fg="white", text="Product management         ", font=("Calibri", 35))
etqTexto.grid(column=1, row=0, padx=12)

idProducto = Label(rojo, text="Id product:", fg="white",bg="IndianRed4", font=("Calibri", 15), height=2)
idProducto.grid(column=0, row=0, padx=5, sticky=W)

name = Label(rojo, text="Name:", fg="white",bg="IndianRed4", font=("Calibri", 15))
name.grid(column=0, row=1, padx=5, sticky=W)

description = Label(rojo, text="Description:", fg="white",bg="IndianRed4", font=("Calibri", 15))
description.grid(column=0, row=2, padx=5, sticky=W)

quantity = Label(rojo, text="quantity:", fg="white",bg="IndianRed4", font=("Calibri", 15))
quantity.grid(column=0, row=3, padx=5, sticky=W)

price = Label(rojo, text="Price:", fg="white",bg="IndianRed4", font=("Calibri", 15))
price.grid(column=0, row=4, padx=5, pady=1, sticky=W)

idEntry = Entry(rojo, bg="IndianRed4", width=30, fg="white")
idEntry.grid(column=1, row=0, padx=20)

nameEntry = Entry(rojo, bg="IndianRed4", width=30, fg="white")
nameEntry.grid(column=1, row=1, padx=20)

descriptionEntry = Entry(rojo, bg="IndianRed4", width=30, fg="white")
descriptionEntry.grid(column=1, row=2, padx=20)

quantityEntry = Entry(rojo, bg="IndianRed4", width=30, fg="white")
quantityEntry.grid(column=1, row=3, padx=20)

priceEntry = Entry(rojo, bg="IndianRed4", width=30, fg="white")
priceEntry.grid(column=1, row=4, padx=20)


save = Button(rojo2, text="Save", fg="white",bg="green", font=("Calibri", 15), width=15)
save.grid(column=0, row=1, pady=6)

delete = Button(rojo2, text="Delete", fg="white",bg="red", font=("Calibri", 15), width=15)
delete.grid(column=0, row=2, pady=5)

update = Button(rojo2, text="Save", fg="white",bg="DarkOrange1", font=("Calibri", 15), width=15)
update.grid(column=0, row=3)


tabla = ttk.Treeview(tablaFrame, height=8, columns=("col1", "col2", "col3", "col4"))
tabla.column("#0", width=105)
tabla.column("col1", width=110, anchor=CENTER)
tabla.column("col2", width=110, anchor=CENTER)
tabla.column("col3", width=110, anchor=CENTER)
tabla.column("col4", width=105, anchor=CENTER)

tabla.heading("#0", text="idproduct", anchor=CENTER)
tabla.heading("col1", text="namep", anchor=CENTER)
tabla.heading("col2", text="description", anchor=CENTER)
tabla.heading("col3", text="quantity", anchor=CENTER)
tabla.heading("col4", text="unite_price", anchor=CENTER)



tabla.insert("", END, text="1", values=("Condia", "lait", "24", "100.0"))
tabla.insert("", END, text="2", values=("la vache quirit", "fromage", "200", "300.0"))
tabla.insert("", END, text="3", values=("hamoud boualam", "boisson gaseuse", "98", "90.0"))
tabla.insert("", END, text="4", values=("Mina", "chocolat", "80", "50.0"))
tabla.insert("", END, text="5", values=("Aroma", "cafe", "60", "80.0"))
tabla.insert("", END, text="6", values=("Facto", "facto", "7000", "600.0"))

tabla.pack()

barra = Scrollbar(tabla, width=17).place(x=523, y=1)



raiz.mainloop()
        


