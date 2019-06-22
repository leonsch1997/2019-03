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
            return True
        except:
            return False

    def modificacion(self, ciudad):
        try:
            ciudad_modificada = self.buscar_x_id_ciudad(ciudad.id_ciudad)
            ciudad_modificada.cod_postal = ciudad.cod_postal
            ciudad_modificada.nombre_ciudad = ciudad.nombre_ciudad
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
        self.message = tk.Label(self.frame, text='Prueba', fg='red')
        self.message.grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E)

        self.mostrar_ciudades()

        # Botones
        boton_alta = ttk.Button(self.frame, text='Agregar Ciudad',
                                command=self.agregar_ciudad
                                ).grid(row=5, column=0, columnspan=1, sticky=tk.W+tk.E)
        boton_modificar = ttk.Button(self.frame, text='Modificar Ciudad',
                                     command=self.eliminar_ciudad
                                ).grid(row=5, column=1, columnspan=1, sticky=tk.W+tk.E)
        boton_eliminar = ttk.Button(self.frame, text='Eliminar Ciudad',
                                    command=self.modificar_ciudad
                                ).grid(row=5, column=2, columnspan=1, sticky=tk.W+tk.E)

        self.mostrar_ciudades()

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
        # try:
        #     self.tabla.item(self.tabla.selection())['text'][0]
        # except IndexError as e:
        #     self.message['text'] = 'Por favor seleccione una ciudad'
        seleccion = ('9999', 'Xxx Xxxxx')
        return seleccion

    def agregar_ciudad(self):
        seleccion = ('', '')
        self.ventana_CRUD('Agregar ciudad', seleccion)

    def agregar_ciudad2(self, ciudad_agregar):
        print('agregar', ciudad_agregar)
        # ciudad = Ciudad()
        # ciudad.cod_postal = ciudad_agregar[0]
        # ciudad.nombre_ciudad = ciudad_agregar[1]
        # datos = DatosCiudades()
        # if datos.alta(ciudad) != False:
        #     self.message['text'] = 'La ciudad {} fue agregada'.format(ciudad_agregar[1])

    def eliminar_ciudad(self):
        seleccion = self.validar_seleccion()
        self.ventana_CRUD('Eliminar ciudad', seleccion)

    def eliminar_ciudad2(self, ciudad_eliminar):
        print('eliminar', ciudad_eliminar)
        # cod_postal_elminar = ciudad_eliminar[0]
        # datos = DatosCiudades()
        # id_ciudad_eliminar = datos.buscar_x_id_ciudad(cod_postal_elminar)
        # if datos.baja(id_ciudad_eliminar):
        #     self.message['text'] = 'La ciudad {} fue eliminada'.format(ciudad_eliminar[1])

    def modificar_ciudad(self):
        seleccion = self.validar_seleccion()
        self.ventana_CRUD('Modificar ciudad', seleccion)

    def modificar_ciudad2(self, ciudad_modificar):
        print('modificar', ciudad_modificar)
        # cod_postal_modificar = ciudad_modificar[0]
        # datos = DatosCiudades()
        # id_ciudad_modificar = datos.buscar_x_id_ciudad(cod_postal_modificar)
        # ciudad_modificacion = datos.buscar_x_id_ciudad(id_ciudad_modificar)
        # if datos.modificacion(ciudad_modificacion) != False:
        #     self.message['text'] = 'La ciudad {} fue agregada'.format(ciudad_modificar[1])

    def ventana_CRUD(self, text_title, seleccion):
        wind_crud = tk.Toplevel()
        wind_crud.title = 'text_title'
        frame_crud = ttk.Frame(wind_crud)
        frame_crud.grid(row=0, column=0, columnspan=3, pady=20)
        self.ciudad_tupla = ('', '')

        # Codigo Postal
        tk.Label(frame_crud, text='Codigo Postal:').grid(row=0, column=1)
        self.cp_nuevo = tk.Entry(frame_crud)  #,
        self.cp_nuevo.grid(row=0, column=2)
            # textvariable=tk.StringVar(wind_crud, value=seleccion[0])).\

        # Ciudad
        tk.Label(frame_crud, text='Ciudad:').grid(row=1, column=1)
        self.ciudad_nueva = tk.Entry(frame_crud)
        self.ciudad_nueva.grid(row=1, column=2)
            #textvariable=tk.StringVar(wind_crud, value=seleccion[1])).\

        def retornar_tupla():
            self.ciudad_tupla = (self.cp_nuevo.get(), self.ciudad_nueva.get())
            wind_crud.destroy()
            if text_title=='Modificar ciudad':
                print('modificar')
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

    # ciudades = datos.todas()
    # for ciudad in ciudades:
    #         print(ciudad[1], '', ciudad[2])

    main_window = tk.Tk()
    app = Ciudades_CodPostales(main_window)
    main_window.mainloop()

###########################

# class Product:
#     # connection dir property
#     db_name = 'database.db'
#
#     def __init__(self, window):
#         # Initializations
#         self.wind = window
#         self.wind.title('Products Application')
#
#         # Creating a Frame Container
#         frame = LabelFrame(self.wind, text = 'Register new Product')
#         frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
#
#         # Name Input
#         Label(frame, text = 'Name: ').grid(row = 1, column = 0)
#         self.name = Entry(frame)
#         self.name.focus()
#         self.name.grid(row = 1, column = 1)
#
#         # Price Input
#         Label(frame, text = 'Price: ').grid(row = 2, column = 0)
#         self.price = Entry(frame)
#         self.price.grid(row = 2, column = 1)
#
#         # Button Add Product
#         ttk.Button(frame, text = 'Save Product', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)
#
#         # Output Messages
#         self.message = Label(text = '', fg = 'red')
#         self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
#
#         # Table
#         self.tree = ttk.Treeview(height = 10, columns = 2)
#         self.tree.grid(row = 4, column = 0, columnspan = 2)
#         self.tree.heading('#0', text = 'Name', anchor = CENTER)
#         self.tree.heading('#1', text = 'Price', anchor = CENTER)
#
#         # Buttons
#         ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
#         ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)
#
#         # Filling the Rows
#         self.get_products()
#
#     # User Input Validation
#     def validation(self):
#         return len(self.name.get()) != 0 and len(self.price.get()) != 0
#
#     def add_product(self):
#         if self.validation():
#             query = 'INSERT INTO product VALUES(NULL, ?, ?)'
#             parameters =  (self.name.get(), self.price.get())
#             self.run_query(query, parameters)
#             self.message['text'] = 'Product {} added Successfully'.format(self.name.get())
#             self.name.delete(0, END)
#             self.price.delete(0, END)
#         else:
#             self.message['text'] = 'Name and Price is Required'
#         self.get_products()
#
#     def delete_product(self):
#         self.message['text'] = ''
#         try:
#            self.tree.item(self.tree.selection())['text'][0]
#         except IndexError as e:
#             self.message['text'] = 'Please select a Record'
#             return
#         self.message['text'] = ''
#         name = self.tree.item(self.tree.selection())['text']
#         query = 'DELETE FROM product WHERE name = ?'
#         self.run_query(query, (name, ))
#         self.message['text'] = 'Record {} deleted Successfully'.format(name)
#         self.get_products()
#
#     def edit_product(self):
#         self.message['text'] = ''
#         try:
#             self.tree.item(self.tree.selection())['values'][0]
#         except IndexError as e:
#             self.message['text'] = 'Please, select Record'
#             return
#         name = self.tree.item(self.tree.selection())['text']
#         old_price = self.tree.item(self.tree.selection())['values'][0]
#         self.edit_wind = Toplevel()
#         self.edit_wind.title = 'Edit Product'
#         # Old Name
#         Label(self.edit_wind, text = 'Old Name:').grid(row = 0, column = 1)
#         Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)
#         # New Name
#         Label(self.edit_wind, text = 'New Price:').grid(row = 1, column = 1)
#         new_name = Entry(self.edit_wind)
#         new_name.grid(row = 1, column = 2)
#
#         # Old Price
#         Label(self.edit_wind, text = 'Old Price:').grid(row = 2, column = 1)
#         Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)
#         # New Price
#         Label(self.edit_wind, text = 'New Name:').grid(row = 3, column = 1)
#         new_price= Entry(self.edit_wind)
#         new_price.grid(row = 3, column = 2)
#
#         Button(self.edit_wind, text = 'Update', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)
#         self.edit_wind.mainloop()
#
#     def edit_records(self, new_name, name, new_price, old_price):
#         query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
#         parameters = (new_name, new_price,name, old_price)
#         self.run_query(query, parameters)
#         self.edit_wind.destroy()
#         self.message['text'] = 'Record {} updated successfylly'.format(name)
#         self.get_products()

