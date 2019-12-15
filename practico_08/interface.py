import tkinter as tk
from tkinter import ttk
import data_modeler
import webbrowser


class ML_inmuebles_UI(tk.Frame):

    def __init__(self, main_window):
        ### Ventana        
        self.wind = main_window
        self.wind.title('Geomapeo propiedades publicadas en Mercado Libre')
        self.wind.resizable(False, False)
        self.pais_seleccionado='Argentina'
        self.data_UI = data_modeler.MLdata()
        self.initUI()

    
    def initUI(self):
        # Crear Frame
        self.frame = ttk.Frame(self.wind)
        self.frame.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
        ### Etiquetas
        self.lb_tipo_inmueble = ttk.Label(self.frame, text='Tipo de Inmueble')
        self.lb_tipo_inmueble.grid(row=0, column=0, columnspan=1, sticky=tk.W)
        self.lb_tipo_operacion = ttk.Label(self.frame, text='Tipo de Operacion')
        self.lb_tipo_operacion.grid(row=0, column=1, columnspan=1, sticky=tk.W)
        self.lb_provincia = ttk.Label(self.frame, text='Provincia')
        self.lb_provincia.grid(row=2, column=0, columnspan=1, pady=(20, 1), sticky=tk.W)
        self.lb_ciudad = ttk.Label(self.frame, text='Ciudad')
        self.lb_ciudad.grid(row=2, column=1, columnspan=1, pady=(20, 1), sticky=tk.W)
        self.lb_barrio = ttk.Label(self.frame, text='Barrio')
        self.lb_barrio.grid(row=2, column=2, columnspan=2, pady=(20, 1), sticky=tk.W)
        ### Lista descolgable 'Tipo de Inmueble' se llena con info que pide 
        # a la capa de negocios
        self.txt_cb_tipo_inmueble = 'Seleccione una opcion'
        self.inmueble_seleccionado = tk.StringVar(value=self.txt_cb_tipo_inmueble)
        self.cb_tipo_inmueble = ttk.Combobox(self.frame, textvariable = self.inmueble_seleccionado, 
                                             height = 10, width=30)
        self.cb_tipo_inmueble.grid(row=1, column=0, columnspan=1, padx=(1, 5), sticky=tk.W)
        self.set_tipo_inmuebles(self.pais_seleccionado)
        ### Lista descolgable 'Tipo de Operacion' se llena con info que pide 
        # # a la capa de negocios
        self.txt_cb_tipo_operacion = 'Seleccione una opcion'
        self.operacion_seleccionada = tk.StringVar(value=self.txt_cb_tipo_operacion)
        self.cb_tipo_operacion = ttk.Combobox(self.frame, textvariable = self.operacion_seleccionada, 
                                              height = 10, width=30)
        self.cb_tipo_operacion.grid(row=1, column=1, columnspan=1, padx=(1, 5), sticky=tk.W)
        self.cb_tipo_operacion.configure(state='disable')
        ### Lista descolgable 'Provincias' se llena con info que pide 
        # a la capa de negocios, al cambiar selección a una provincia,
        # pide info ciudades a la capa de negocio y habilita lista descolgable 'Ciudades'
        self.txt_cb_provincia = 'Seleccione una provincia'
        self.provincia_seleccionada = tk.StringVar(value=self.txt_cb_provincia)
        self.cb_provincia = ttk.Combobox(self.frame, textvariable = self.provincia_seleccionada, 
                                         height = 10, width=30)
        self.cb_provincia.grid(row=3, column=0, columnspan=1, padx=(1, 5), sticky=tk.W)
        self.cb_provincia.configure(state='disable')
        ### Lista descolgable 'Cuidades', al cambiar selección a una ciudad,
        # pide info ciudades a la capa de negocio y habilita lista descolgable 'Ciudades'
        self.txt_cb_ciudad = 'Seleccione una ciudad'
        self.ciudad_seleccionada = tk.StringVar(value=self.txt_cb_ciudad)
        self.cb_ciudad = ttk.Combobox(self.frame, textvariable = self.ciudad_seleccionada, 
                                      height = 10, width=30)
        self.cb_ciudad.grid(row=3, column=1, columnspan=1, padx=(1, 5), sticky=tk.W)
        self.cb_ciudad.configure(state='disable')
        ### Lista descolgable 'Barrios', la selección de un barrio es opcional
        self.barrio_seleccionado = tk.StringVar(value='Opcionalemente seleccione un barrio')
        self.cb_barrio = ttk.Combobox(self.frame, textvariable = self.barrio_seleccionado, 
                                      height = 10, width=35)
        self.cb_barrio.grid(row=3, column=2, columnspan=2, padx=(1, 5), sticky=tk.W)
        self.cb_barrio.configure(state='disable')
        ### Manejo de los eventos de seleccion de los comboboxes
        self.cb_tipo_inmueble.bind('<<ComboboxSelected>>', self.set_tipo_operaciones)
        self.cb_tipo_operacion.bind('<<ComboboxSelected>>', self.set_provincias)
        self.cb_provincia.bind('<<ComboboxSelected>>', self.set_ciudades)
        self.cb_ciudad.bind('<<ComboboxSelected>>', self.set_barrios)
        ### Boton 'Cancelar' cierra programa/ventana
        self.boton_cancelar = tk.Button(self.frame, text='Cancelar', command=self.cerrar_ventana)
        self.boton_cancelar.grid(row=4, column=2, pady=(20, 1), padx=(1, 5), sticky=tk.E)
        ### Boton 'Generar Mapa' pasa seleccion a capa de negocios
        self.boton_confirmar = tk.Button(self.frame, text='Generar Mapa', command=self.generate_map)
        self.boton_confirmar.grid(row=4, column=3, pady=(20, 1), padx=(1, 5), sticky=tk.W)
        self.boton_confirmar.configure(state='disable')

    ## Funcion que establece el listado de tipo de inmuebles en su combobox
    def set_tipo_inmuebles(self, pais):
        self.cb_tipo_inmueble['values']= self.data_UI.get_tipos_inmueble(pais)
        self.cb_tipo_inmueble.configure(state='readonly')

    ## Funcion que establece el listado de tipo de operaciones en su combobox
    def set_tipo_operaciones(self, event):
        if str(self.inmueble_seleccionado.get()) != self.txt_cb_tipo_inmueble:
            self.cb_tipo_operacion['values'] = self.data_UI.get_tipos_operacion(str(self.inmueble_seleccionado.get()))
            self.cb_tipo_operacion.configure(state='readonly')

    ## Funcion que establece el listado provincias en su combobox
    def set_provincias(self, event):
        if str(self.operacion_seleccionada.get()) != self.txt_cb_tipo_operacion:
            self.cb_provincia['values']= self.data_UI.get_provincias(self.pais_seleccionado)
            self.cb_provincia.configure(state='readonly')

    ## Funcion que establece el listado ciudades en su combobox
    def set_ciudades(self, event):
        if str(self.provincia_seleccionada.get()) != self.txt_cb_provincia:
            self.cb_ciudad['values']= self.data_UI.get_ciudades(str(self.provincia_seleccionada.get()))
            self.cb_ciudad.configure(state='readonly')
            self.boton_confirmar.configure(state='active')            

    ## Funcion que establece el listado barrios en su combobox
    def set_barrios(self, event):
        if str(self.ciudad_seleccionada.get()) != self.txt_cb_ciudad:
            self.cb_barrio['values']= self.data_UI.get_barrios(str(self.ciudad_seleccionada.get()))
            self.cb_barrio.configure(state='readonly')

    
    ## Funcion llamada por el boton 'Generar Mapa'
    def generate_map(self):
        seleccion = (str(self.inmueble_seleccionado.get()),
                     str(self.operacion_seleccionada.get()),
                     str(self.provincia_seleccionada.get()),
                     str(self.ciudad_seleccionada.get()),
                     str(self.barrio_seleccionado.get())
                    )
        print('Mapa: ', seleccion)
        self.data_UI.generate_map(seleccion)
        webbrowser.open_new_tab('map_created.html')
        self.wind.destroy()
        
    ## Funcion llamada por el boton 'Cancelar'
    def cerrar_ventana(self):
        self.wind.destroy()



if __name__ == '__main__':
    main_window = tk.Tk()
    app = ML_inmuebles_UI(main_window)
    main_window.mainloop()


