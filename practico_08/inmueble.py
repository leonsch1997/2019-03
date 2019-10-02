class inmueble:
    mercadolibre_id = 'MLA79242'
    tabla = 'mercadolibre_inmueble' # Utilizada para la carga en SQL Server
    columnas = ['titulo', 'producto_latitud', 'producto_longitud', 'url'
                'tipo_propiedad']
 
    # Conversion de json a dataframe y rearmado de datos para que sea formato tabla
    def adapt(self, items):
        data = pd.DataFrame(items)
        data = data.groupby(['id']).first().reset_index() # Elimina duplicados
 
        largo = data.shape[0]
        for i in range(0, largo):
            if(i % 100 == 0): print("Procesando: " + str(i) + " de " + str(largo))
            try:
                data.loc[i,'fecha'] = strftime("%Y_%m_%d", gmtime())
                data.loc[i,'producto_latitud'] = data.loc[i,'location']['latitude']
                data.loc[i,'producto_longitud'] = data.loc[i,'location']['longitude']
                data.loc[i,'url'] = data.loc[i,'permalink']
                dataAttr = pd.DataFrame(data.loc[i,'attributes'])
                if(dataAttr.loc[dataAttr['id']=='PROPERTY_TYPE']['value_name'].count() > 0):
                    data.loc[i,'tipo_propiedad'] = dataAttr.loc[dataAttr['id']=='PROPERTY_TYPE']['value_name'].item()
                else:
                    data.loc[i,'tipo_propiedad'] = 'DESCONOCIDO'
 
            except Exception as e:
                print('Error adaptando: ' + str(i) + ' - ' + str(data.loc[i,'mercadolibre_id']) + ' - ' + ' -- %s' % e)
                pass            
        data = data.fillna('') # Los nulos los completamos con un string vacio
        return data[self.columnas]