## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones
## 1- un  botón  Alta que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra .

import tkinter as tk
from tkinter import ttk
class CreaFrame(tk.Frame):
    def __init__(self, padre=None, titulo =''): #--- recibe un form contenedor ‘padre’
        super().__init__(padre)
        self.padre = padre
        self.grid(column=0, row=0,padx=(50,50), pady=(10,10))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.agregar_ciudades()

    def agregar_ciudades(self):
        self.treeview = ttk.Treeview(self, columns=("C.P"))
        self.treeview.pack()
        self.treeview.heading("#0",text="Ciudades")
        self.treeview.heading("C.P",text="Codigo Postal")
        self.treeview.insert("", tk.END,text="Rosario",values=("2000"))
        self.treeview.insert("", tk.END,text="Casilda",values=("2170"))
        self.treeview.insert("", tk.END,text="Buenos Aires",values=("1000"))
        self.treeview.insert("", tk.END,text="Cordoba",values=("5000"))
        self.treeview.insert("", tk.END,text="Mar del plata",values=("7600"))

        self.botonalta=tk.Button(self,text="Alta",command=self.alta)
        self.botonalta.pack()
        """self.botonbaja=tk.Button(self,text="Baja",command=self.baja)
        self.botonbaja.pack()
        self.botonmod=tk.Button(self,text="Modifica",command=self.modifica)
        self.botonmod.pack()"""

    def alta(self):
        ciu=input("ingrese nombre de la ciudad")
        cod=input("ingrese codigo postal")
        self.treeview.insert("", tk.END,text=ciu,values=cod)


if __name__ == '__main__':
    form1 = tk.Tk()
    app = CreaFrame(padre=form1, titulo='Ciudades')
    form1.mainloop()
