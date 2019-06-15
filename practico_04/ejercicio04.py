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
        self.ciu= tk.StringVar()
        self.cod= tk.StringVar()
        self.valorciudad=tk.StringVar()
        self.valorcodigo=tk.StringVar()

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
        self.botonalta.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
        """self.botonbaja=tk.Button(self,text="Baja",command=self.baja)
        self.botonbaja.pack()
        self.botonmod=tk.Button(self,text="Modifica",command=self.modifica)
        self.botonmod.pack()"""

    def alta(self):
        self.abrirventana2()

    def abrirventana2(self):
        self.padre.deiconify()
        win=tk.Toplevel()
        win.geometry('380x300+50+20')
        win.config(background='light blue')
        labelciudad=tk.Label(win,text="Ingrese nombre de la ciudad",background='light blue')
        labelciudad.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
        win.ciud=tk.Entry(win,justify="center",textvariable=self.ciu)
        win.ciud.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)

        labelcod=tk.Label(win,text="Ingrese codigo postal (CP)",background='light blue')
        labelcod.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
        win.codi=tk.Entry(win,justify="center",textvariable=self.cod)
        win.codi.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)


        btnAgrega=tk.Button(win,text="Agregar",justify='center',command=self.agregar())
        btnAgrega.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)

    def agregar(self):
        try:
            valu1=self.valorciudad.set(str(self.abrirventana2.win.ciud.get()))
            valu2=self.valorcodigo.set(str(self.abrirventana2.win.codi.get()))
            self.treeview.insert("", tk.END,text=valu1,values=valu2)
        except:
            ValueError(print("ERROR! no se ingreso alguno de los valores!"))

if __name__ == '__main__':
    form1 = tk.Tk()
    app = CreaFrame(padre=form1, titulo='Ciudades')
    form1.mainloop()
