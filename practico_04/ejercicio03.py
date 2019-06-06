## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) .
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
if __name__ == '__main__':
    form1 = tk.Tk()
    app = CreaFrame(padre=form1, titulo='Ciudades')
    form1.mainloop()
