import tkinter as tk
from tkinter import ttk
from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, MaximoAlcanzado, DniRepetido

class Socios_CP(tk.Frame):

    def __init__(self, main_window):
        self.wind = main_window
        self.wind.title('Socios')

        # Crear Frame

        self.frame = ttk.Frame(self.wind)
        self.frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Tabla
        self.tabla = ttk.Treeview(self.frame, height=10, columns=("#1", "#2","#3"))
        self.tabla.grid(row=4, column=0, columnspan=3)
        self.tabla.heading('#0', text='ID_Socio', anchor=tk.CENTER)
        self.tabla.heading("#1", text='Apellido', anchor=tk.CENTER)
        self.tabla.heading("#2", text='Nombre', anchor=tk.CENTER)
        self.tabla.heading("#3", text='DNI', anchor=tk.CENTER)

        #Mensaje
        self.message = tk.Label(self.frame, text='', fg='red')
        self.message.grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E)

        self.mostrar_socios()

        # Botones
        boton_alta = ttk.Button(self.frame, text='Agregar Socio',
                                command=self.agregar_socio
                                ).grid(row=5, column=0, columnspan=1, sticky=tk.W+tk.E)
        boton_modificar = ttk.Button(self.frame, text='Modificar Socio',
                                     command=self.modificar_socio
                                ).grid(row=5, column=1, columnspan=1, sticky=tk.W+tk.E)
        boton_eliminar = ttk.Button(self.frame, text='Eliminar Socio',
                                    command=self.eliminar_socio
                                ).grid(row=5, column=2, columnspan=1, sticky=tk.W+tk.E)


    def mostrar_socios(self):
        # cleaning Table
        filas = self.tabla.get_children()
        for fila in filas:
            self.tabla.delete(fila)
        # getting data
        datos = NegocioSocio()
        filas = datos.todos()

        # filling data
        for fila in filas:
            self.tabla.insert('', 0, text=fila.id_socio, values=(fila.apellido, fila.nombre, fila.dni))

    def validar_seleccion(self):
        socio_validado = Socio()
        try:
            socio_validado.id_socio = self.tabla.item(self.tabla.selection())['text']
            socio_validado.apellido = self.tabla.item(self.tabla.selection())['values'][0]
            socio_validado.nombre = self.tabla.item(self.tabla.selection())['values'][1]
            socio_validado.dni = self.tabla.item(self.tabla.selection())['values'][2]
        except IndexError as e:
            self.message['text'] = 'Por favor seleccione un socio'
        return socio_validado

    def agregar_socio(self):
        socio_nuevo = Socio()
        self.ventana_CRUD('Agregar Socio', socio_nuevo)

    def agregar_socio2(self, socio_agregar):
        try:
            datos = NegocioSocio()
            if datos.alta(socio_agregar):
                self.message['text'] = 'El socio {0}, {1} fue agregado'.format(socio_agregar.apellido,
                                                                               socio_agregar.nombre)
            self.mostrar_socios()
        except Exception as e:
            self.message['text'] = 'El socio {0}, {1} NO fue agregado. {2}'.format(socio_agregar.apellido,
                                                                                   socio_agregar.nombre,
                                                                                   str(e))

    def eliminar_socio(self):
        socio_seleccionado = self.validar_seleccion()
        if socio_seleccionado.id_socio != '':
            self.ventana_CRUD('Eliminar Socio', socio_seleccionado)

    def eliminar_socio2(self, socio_eliminar):
        datos = NegocioSocio()
        if datos.baja(socio_eliminar.id_socio):
            self.message['text'] = 'El socio {0}, {1} fue eliminado'.format(socio_eliminar.apellido, socio_eliminar.nombre)
        self.mostrar_socios()

    def modificar_socio(self):
        socio_seleccionado = self.validar_seleccion()
        if socio_seleccionado.id_socio != '':
            self.ventana_CRUD('Modificar Socio', socio_seleccionado)

    def modificar_socio2(self, socio_modificar):
        try:
            datos = NegocioSocio()
            if datos.modificacion(socio_modificar) == True:
                self.message['text'] = 'El socio {0}, {1} fue modificado'.format(socio_modificar.apellido, socio_modificar.nombre)
            self.mostrar_socios()
        except Exception as e:
            self.message['text'] = 'El socio {0}, {1} NO fue modificado. {2}'.format(socio_modificar.apellido,
                                                                                   socio_modificar.nombre,
                                                                                   str(e))

    def ventana_CRUD(self, text_title, socio_seleccionado):
        self.message['text'] = ''
        wind_crud = tk.Toplevel()
        wind_crud.title = 'text_title'
        frame_crud = ttk.Frame(wind_crud)
        frame_crud.grid(row=0, column=0, columnspan=4, pady=20)
        tk.Label(frame_crud, text=text_title).grid(row=0, column=1, columnspan=4)
        id_socio = tk.StringVar(frame_crud, value=socio_seleccionado.id_socio)
        apellido_socio = tk.StringVar(frame_crud, value=socio_seleccionado.apellido)
        nombre_socio = tk.StringVar(frame_crud, value=socio_seleccionado.nombre)
        dni_socio = tk.StringVar(frame_crud, value=socio_seleccionado.dni)

        # id socio
        tk.Label(frame_crud, text='ID Socio:').grid(row=1, column=1)
        self.id_nuevo = tk.Entry(frame_crud, textvariable=id_socio)
        self.id_nuevo.grid(row=1, column=2)
        self.id_nuevo.configure(state='readonly')

        # apellido_socio
        tk.Label(frame_crud, text='Apellido:').grid(row=2, column=1)
        self.apellido_nuevo = tk.Entry(frame_crud, textvariable=apellido_socio)
        self.apellido_nuevo.grid(row=2, column=2)
        if text_title=='Eliminar Socio':
            self.apellido_nuevo.configure(state='readonly')

        # nombre_socio
        tk.Label(frame_crud, text='Nombre:').grid(row=3, column=1)
        self.nombre_nuevo = tk.Entry(frame_crud, textvariable=nombre_socio)
        self.nombre_nuevo.grid(row=3, column=2)
        if text_title=='Eliminar Socio':
            self.nombre_nuevo.configure(state='readonly')

        # dni_socio
        tk.Label(frame_crud, text='DNI:').grid(row=4, column=1)
        self.dni_nuevo = tk.Entry(frame_crud, textvariable=dni_socio)
        self.dni_nuevo.grid(row=4, column=2)
        if text_title=='Eliminar Socio':
            self.dni_nuevo.configure(state='readonly')

        def retornar_socio():
            socio = Socio()
            if text_title=='Modificar Socio':
                socio.id_socio = socio_seleccionado.id_socio
                socio.apellido = self.apellido_nuevo.get()
                socio.nombre = self.nombre_nuevo.get()
                socio.dni = self.dni_nuevo.get()
                self.modificar_socio2(socio)
            if text_title=='Eliminar Socio':
                self.eliminar_socio2(socio_seleccionado)
            if text_title=='Agregar Socio':
                socio.apellido = self.apellido_nuevo.get()
                socio.nombre = self.nombre_nuevo.get()
                socio.dni = self.dni_nuevo.get()
                self.agregar_socio2(socio)
            wind_crud.destroy()

        def retornar_cancelar():
            wind_crud.destroy()

        # Botones
        boton_confirmar = tk.Button(wind_crud, text='Confirmar', command=retornar_socio).\
            grid(row=5, column=0, sticky=tk.W)
        boton_cancelar = tk.Button(wind_crud, text='Cancelar', command=retornar_cancelar).\
            grid(row=5, column=3, sticky=tk.E)

        wind_crud.mainloop()


if __name__ == '__main__':
    # for x in range(1,10):
    #         ns = NegocioSocio()
    #         socio = Socio(dni=x, nombre='Juan', apellido='Perez')
    #         exito = ns.alta(socio)
    main_window = tk.Tk()
    app = Socios_CP(main_window)
    main_window.mainloop()
