## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones
## 1- un  botón  Alta que inicia otra venta donde puedo ingresar una ciudad y
# su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada
# en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista
# que se muestra .

import tkinter as tk
from tkinter import ttk
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, inspect, create_engine, inspect
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Ciudad(Base):
    __tablename__ = 'ciudades'
    id_ciudad = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    cod_postal = Column(Integer)
    nombre_ciudad = Column(String(200))


class DatosCiudades(object):

    def __init__(self):
        engine = create_engine('sqlite:///ciudades.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

        ins = inspect(engine)
        t_exists = False
        for t in ins.get_table_names():
            if t == 'ciudades':
                t_exists = True
        if t_exists == False:
            Ciudad.__table__.create()

    def buscar_x_id_ciudad(self, id_ciudad_buscado):
        try:
            ciudad = self.session.query(Ciudad).get(id_ciudad_buscado)
            return ciudad
        except:
            return None

    def buscar_x_cod_postal(self, cod_postal_buscado):
        try:
            ciudad = self.session.query(Ciudad).filter(Ciudad.cod_postal==cod_postal_buscado).first()
            return ciudad.id_ciudad
        except:
            return None

    def todas(self):
        ciudades = self.session.query(Ciudad).all()
        lista_ciudades = []
        for c in ciudades:
            lista_ciudades.append((c.id_ciudad, c.cod_postal, c.nombre_ciudad))
        return lista_ciudades

    def borrar_todas(self):
        try:
            self.session.query(Ciudad).delete()
            return True
        except:
            return False

    def alta(self, ciudad):
        try:
            self.session.add(ciudad)
            self.session.commit()
            return ciudad
        except:
            return False

    def baja(self, id_ciudad_baja):
        try:
            ciudad = self.buscar_x_id_ciudad(id_ciudad_baja)
            self.session.delete(ciudad)
            self.session.commit()
            return True
        except:
            return False

    def modificacion(self, id_ciudad, cod_postal, nombre_ciudad):
        try:
            ciudad_modificada = self.buscar_x_id_ciudad(id_ciudad)
            ciudad_modificada.cod_postal = cod_postal
            ciudad_modificada.nombre_ciudad = nombre_ciudad
            self.session.commit()
            return ciudad_modificada
        except:
            return False


class Ciudades_CodPostales(tk.Frame):

    def __init__(self, main_window):
        self.wind = main_window
        self.wind.title('Ciudades y Codigos Postales')

        # Crear Frame

        self.frame = ttk.Frame(self.wind)
        self.frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Tabla
        self.tabla = ttk.Treeview(self.frame, height=10, columns=2)
        self.tabla.grid(row=4, column=0, columnspan=3)
        self.tabla.heading('#0', text='Codigo Postal', anchor=tk.CENTER)
        self.tabla.heading('#1', text='Ciudad', anchor=tk.CENTER)

        #Mensaje
        self.message = tk.Label(self.frame, text='', fg='red')
        self.message.grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E)

        self.mostrar_ciudades()

        # Botones
        boton_alta = ttk.Button(self.frame, text='Agregar Ciudad',
                                command=self.agregar_ciudad
                                ).grid(row=5, column=0, columnspan=1, sticky=tk.W+tk.E)
        boton_modificar = ttk.Button(self.frame, text='Modificar Ciudad',
                                     command=self.modificar_ciudad
                                ).grid(row=5, column=1, columnspan=1, sticky=tk.W+tk.E)
        boton_eliminar = ttk.Button(self.frame, text='Eliminar Ciudad',
                                    command=self.eliminar_ciudad
                                ).grid(row=5, column=2, columnspan=1, sticky=tk.W+tk.E)


    def mostrar_ciudades(self):
        # cleaning Table
        filas = self.tabla.get_children()
        for fila in filas:
            self.tabla.delete(fila)
        # getting data
        ciudades = DatosCiudades()
        filas = ciudades.todas()
        # filling data
        for fila in filas:
            self.tabla.insert('', 0, text=fila[1], values=(fila[2],))

    def validar_seleccion(self):
        seleccion = ('', '')
        try:
            datos = DatosCiudades()
            id_seleccion = datos.buscar_x_cod_postal(self.tabla.item(self.tabla.selection())['text'])
            seleccion = (id_seleccion, self.tabla.item(self.tabla.selection())['text'],
                         self.tabla.item(self.tabla.selection())['values'][0])
        except IndexError as e:
            self.message['text'] = 'Por favor seleccione una ciudad'
        return seleccion

    def agregar_ciudad(self):
        seleccion = ('', '', '')
        self.ventana_CRUD('Agregar ciudad', seleccion)

    def agregar_ciudad2(self, ciudad_agregar):
        ciudad = Ciudad()
        ciudad.cod_postal = ciudad_agregar[1]
        ciudad.nombre_ciudad = ciudad_agregar[2]
        datos = DatosCiudades()
        if datos.alta(ciudad) != False:
            self.message['text'] = 'La ciudad {} fue agregada'.format(ciudad_agregar[2])
        self.mostrar_ciudades()

    def eliminar_ciudad(self):
        seleccion = self.validar_seleccion()
        if seleccion != ('', ''):
            self.ventana_CRUD('Eliminar ciudad', seleccion)

    def eliminar_ciudad2(self, ciudad_eliminar):
        if datos.baja(ciudad_eliminar[0]):
            self.message['text'] = 'La ciudad {} fue eliminada'.format(ciudad_eliminar[2])
        self.mostrar_ciudades()

    def modificar_ciudad(self):
        seleccion = self.validar_seleccion()
        if seleccion != ('', ''):
            self.ventana_CRUD('Modificar ciudad', seleccion)

    def modificar_ciudad2(self, ciudad_modificar):
        if datos.modificacion(ciudad_modificar[0],
                              ciudad_modificar[1],
                              ciudad_modificar[2]) != False:
            self.message['text'] = 'La ciudad {} fue modificada'.format(ciudad_modificar[2])
        self.mostrar_ciudades()

    def ventana_CRUD(self, text_title, seleccion):
        self.message['text'] = ''
        wind_crud = tk.Toplevel()
        wind_crud.title = 'text_title'
        frame_crud = ttk.Frame(wind_crud)
        frame_crud.grid(row=0, column=0, columnspan=3, pady=20)
        tk.Label(frame_crud, text=text_title).grid(row=0, column=1, columnspan=3)
        self.ciudad_tupla = ('', '')
        cp_default = tk.StringVar(frame_crud, value=seleccion[1])
        nombre_ciudad = tk.StringVar(frame_crud, value=seleccion[2])

        # Codigo Postal
        tk.Label(frame_crud, text='Codigo Postal:').grid(row=1, column=1)
        self.cp_nuevo = tk.Entry(frame_crud, textvariable=cp_default)
        self.cp_nuevo.grid(row=1, column=2)
        if text_title=='Eliminar ciudad':
            self.cp_nuevo.configure(state='readonly')

        # Ciudad
        tk.Label(frame_crud, text='Ciudad:').grid(row=2, column=1)
        self.ciudad_nueva = tk.Entry(frame_crud, textvariable=nombre_ciudad)
        self.ciudad_nueva.grid(row=2, column=2)
        if text_title=='Eliminar ciudad':
            self.ciudad_nueva.configure(state='readonly')

        def retornar_tupla():
            self.ciudad_tupla = (seleccion[0], self.cp_nuevo.get(), self.ciudad_nueva.get())
            wind_crud.destroy()
            if text_title=='Modificar ciudad':
                self.modificar_ciudad2(self.ciudad_tupla)
            if text_title=='Eliminar ciudad':
                self.eliminar_ciudad2(self.ciudad_tupla)
            if text_title=='Agregar ciudad':
                self.agregar_ciudad2(self.ciudad_tupla)

        def retornar_cancelar():
            wind_crud.destroy()

        # Botones
        boton_confirmar = tk.Button(wind_crud, text='Confirmar', command=retornar_tupla).\
            grid(row=4, column=0, sticky=tk.W)
        boton_cancelar = tk.Button(wind_crud, text='Cancelar', command=retornar_cancelar).\
            grid(row=4, column=3, sticky=tk.E)
        wind_crud.mainloop()


if __name__ == '__main__':
    # carga datos ciudades
    datos = DatosCiudades()
    datos.borrar_todas()
    ciudad = Ciudad()
    ciudad.cod_postal = 2000
    ciudad.nombre_ciudad = 'Rosario'
    datos.alta(ciudad)
    ciudad2 = Ciudad()
    ciudad2.cod_postal = 3000
    ciudad2.nombre_ciudad = 'Cordoba'
    datos.alta(ciudad2)
    ciudad3 = Ciudad()
    ciudad3.cod_postal = 1000
    ciudad3.nombre_ciudad = 'Ciudad Autonoma de Buenos Aires'
    datos.alta(ciudad3)

    main_window = tk.Tk()
    app = Ciudades_CodPostales(main_window)
    main_window.mainloop()


