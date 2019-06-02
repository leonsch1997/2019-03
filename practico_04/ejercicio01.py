## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .
import tkinter as tk

class CreaFrame(tk.Frame):
    def __init__(self, padre=None, titulo =''): #--- recibe un form contenedor ‘padre’
        super().__init__(padre)
        self.padre = padre
        self.pack(side='top')
        self.crear_controles(titulo)
    def crear_controles(self, titulo):
        v1=tk.StringVar()
        v2=tk.StringVar()
        res=float
        self.lblTitulo = tk.Label(self, text=titulo)
        self.lblTitulo.pack()
        self.num1Label= tk.Label(self,text='Primero numero')
        self.num1Label.pack(side="top")
        self.n1=tk.Entry(self,textvariable=v1)
        self.n1.pack(side="top")
        self.num2Label= tk.Label(self,text='Segundo numero')
        self.num2Label.pack(side="top")
        self.n2=tk.Entry(self,textvariable=v2)
        self.n2.pack(side="top")
        self.btn_suma = tk.Button(self,text='+',command=self.suma) #--- el padre es un frame
        self.btn_suma.pack(side="left")
        self.btn_resta = tk.Button(self,text='-',command=self.resta)
        self.btn_resta.pack(side="left")
        self.btn_multiplica = tk.Button(self,text='x',command=self.multiplica)
        self.btn_multiplica.pack(side="left")
        self.btn_divide = tk.Button(self,text='/',command=self.divide)
        self.btn_divide.pack(side="left")
    def suma(self):
        try:
            res=(float(self.n1.get())+float(self.n2.get()))
            print (res)
        except:
            ValueError(print("ERROR! no se ingreso alguno de los valores!"))
    def resta(self):
        try:
            res=(float(self.n1.get())-float(self.n2.get()))
            print (res)
        except:
            ValueError(print("ERROR! no se ingreso alguno de los valores!"))
    def multiplica(self):
        try:
            res=(float(self.n1.get())*float(self.n2.get()))
            print (res)
        except:
            ValueError(print("ERROR! no se ingreso alguno de los valores!"))
    def divide(self):
        try:
            res=(float(self.n1.get())/float(self.n2.get()))
            print (res)
        except:
            ValueError(print("ERROR! no se ingreso alguno de los valores!"))
if __name__ == '__main__':
    form1 = tk.Tk()
    app = CreaFrame(padre=form1, titulo='Calculadora')
    form1.mainloop()
