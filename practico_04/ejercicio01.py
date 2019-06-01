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
        self.n1=tk.Entry(self,textvariable=v1)
        self.n2=tk.Entry(self,textvariable=v2)
        self.n1.pack(side="top")
        self.n2.pack(side="left")
        self.btn_suma = tk.Button(self,text='+',command=self.suma) #--- el padre es un frame
        self.btn_suma.pack(side="right")
        self.btn_resta = tk.Button(self,text='-',command=self.resta)
        self.btn_resta.pack(side="right")
        self.btn_multiplica = tk.Button(self,text='x',command=self.multiplica)
        self.btn_multiplica.pack(side="right")
        self.btn_divide = tk.Button(self,text='/',command=self.divide)
        self.btn_divide.pack(side="right")
        self.btn_salir = tk.Button(self, text="QUIT", fg="red",command=self.padre.destroy) #--- se cierra el form padre
        self.btn_salir.pack(side="bottom")

    def suma(self):
        res=(float(self.n1.get())+float(self.n2.get()))
        print(res)
    def resta(self):
        res=(float(self.n1.get())-float(self.n2.get()))
        print(res)
    def multiplica(self):
        res=(float(self.n1.get())*float(self.n2.get()))
        print(res)
    def divide(self):
        res=(float(self.n1.get())/float(self.n2.get()))
        print(res)
if __name__ == '__main__':
    form1 = tk.Tk()
    app = CreaFrame(padre=form1, titulo='Calculadora')   
    form1.mainloop()

