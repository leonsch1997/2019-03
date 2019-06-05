## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .
import tkinter as tk
from tkinter import ttk
class CreaFrame(tk.Frame):
    def __init__(self, padre=None, titulo =''): #--- recibe un form contenedor ‘padre’
        super().__init__(padre)
        self.padre = padre
        self.grid(column=0, row=0,padx=(50,50), pady=(10,10))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.crear_controles(titulo)

    def borrar(self):
        self.v1.set("")
        self.v2.set("")
    def suma(self):
        try:
            self.res.set(float(self.n1.get())+float(self.n2.get()))
            self.borrar()
        except:
            ValueError(print("ERROR! no se ingreso alguno de los valores!"))
    def resta(self):
        try:
            self.res.set(float(self.n1.get())-float(self.n2.get()))
            self.borrar()
        except:
            ValueError(print("ERROR! no se ingreso alguno de los valores!"))
    def multiplica(self):
        try:
            self.res.set(float(self.n1.get())*float(self.n2.get()))
            self.borrar()
        except:
            ValueError(print("ERROR! no se ingreso alguno de los valores!"))
    def divide(self):
        try:
            self.res.set(float(self.n1.get())/float(self.n2.get()))
            self.borrar()
        except:
            ValueError(print("ERROR! no se ingreso alguno de los valores!"))


    def crear_controles(self, titulo):
        self.v1 = tk.StringVar()
        self.v2 = tk.StringVar()
        self.res = tk.StringVar()

        self.lblTitulo = tk.Label(self, text=titulo)
        self.lblTitulo.pack()

        self.num1Label= tk.Label(self,text='Primero numero')
        self.num1Label.pack(side="top")
        self.n1=ttk.Entry(self,justify="center",textvariable=self.v1)
        self.n1.pack(side="top")

        self.num2Label= tk.Label(self,text='Segundo numero')
        self.num2Label.pack(side="top")
        self.n2=ttk.Entry(self,justify="center",textvariable=self.v2)
        self.n2.pack(side="top")

        """Sumar"""
        self.btn_suma = tk.Button(self,text='+',command=self.suma)
        self.btn_suma.pack(side="left",padx=10,pady=10)

        """Restar"""
        self.btn_resta = tk.Button(self,text='-',command=self.resta)
        self.btn_resta.pack(side="left",padx=10,pady=10)

        """Multiplicar"""
        self.btn_multiplica = tk.Button(self,text='x',command=self.multiplica)
        self.btn_multiplica.pack(side="left",padx=10,pady=10)

        """Dividir"""
        self.btn_divide = tk.Button(self,text='/',command=self.divide)
        self.btn_divide.pack(side="left",padx=10,pady=10)

        self.separ=tk.Label(self, text="").pack() #Separador

        """Resultado"""
        self.resul=ttk.Entry(self,justify="center",state="disabled",textvariable=self.res).pack(side="bottom")
        self.resultado= tk.Label(self,text='Resultado: ')
        self.resultado.pack(side="bottom")


if __name__ == '__main__':
    form1 = tk.Tk()
    app = CreaFrame(padre=form1, titulo='Calculadora')
    form1.mainloop()
