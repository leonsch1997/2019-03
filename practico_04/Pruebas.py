import tkinter as tk
from tkinter import ttk
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, inspect, create_engine, inspect
from sqlalchemy.orm import sessionmaker


class Prueba(tk.Frame):
    def __init__(self, main_window):
        self.wind = main_window
        self.wind.title('Ciudades y Codigos Postales')

        # Crear Frame
        self.frame = tk.Frame(self.wind)
        self.frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Name Input
        ttk.Label(self.frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = ttk.Entry(self.frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        self.contenido = ''

        def imprimir_label():
            self.contenido = self.name.get()
            if self.contenido == '':
                print('Contenido Vacio')
            else:
                print(self.contenido)

        # Boton
        boton_alta = ttk.Button(self.frame, text='Agregar Ciudad',
                                command=imprimir_label
                                ).grid(row=5, column=0, columnspan=1, sticky=tk.W+tk.E)



if __name__ == '__main__':
    main_window = tk.Tk()
    app = Prueba(main_window)
    main_window.mainloop()
