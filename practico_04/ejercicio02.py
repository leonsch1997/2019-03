## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

from tkinter import *

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="white")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculadora')

        display = StringVar()

        Entry(self, relief=FLAT, textvariable=display, justify='right', bd=2, bg="powder blue"
              ).pack(side=TOP, expand=YES, fill=BOTH)

        for clearBut in (["CE"],["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))

        for numBut in ("789/", "456*", "123-", "0.+"):
            numeros = iCalc(self, TOP)
            for char in numBut:
                button(numeros, LEFT, char,
                       lambda storeObj=display, q=char: storeObj.set(storeObj.get()+q))

        equal_button = iCalc(self, TOP)
        for iequals in "=":
            if iequals == "=":
                btni_Equals = button(equal_button, LEFT, iequals)
                btni_Equals.bind('<ButtonRelease-1>',
                                 lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btni_Equals = button(equal_button, LEFT, iequals,
                                     lambda storeObj= display, s='%s '%iequals: storeObj.set(storeObj.get()+s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    app().mainloop()


