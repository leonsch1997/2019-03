import ml_scrapperAPI
import pandas
import locale
import mapper
import geeklab_dollarAPI

class MLdata:
    def __init__(self):
        self.data_scrapper = ml_scrapperAPI.ML_API()
        self.cod_site = ''
        self.cod_category = ''
        self.cod_tipo_inmueble = ''
        self.cod_tipo_operacion = ''

    ## Funcion que pide a la capa de datos listado de 'Tipo de Inmueble',
    # y devuelve lista a la capa de presentacion
    def get_tipos_inmueble(self, pais):
        pDF_sites = self.data_scrapper.sites()
        self.cod_site = list(pDF_sites[pDF_sites.name == pais]['id'])[0] #String
        pDF_categories = self.data_scrapper.categorias_Xsite(self.cod_site)
        self.cod_category = list(pDF_categories[pDF_categories.name == 'Inmuebles']['id'])[0] #String
        pDF_subcat_inmuebles = self.data_scrapper.subcategoria_Xcategoria(self.cod_category)
        lst_tipos_inmuebles = list(pDF_subcat_inmuebles['name'])
        return lst_tipos_inmuebles

    ## Funcion que pide a la capa de datos listado de 'Tipo de Operacion',
    # y devuelve listado a la capa de presentacion
    def get_tipos_operacion(self, tipo_inmueble):
        pDF_subcat_inmuebles = self.data_scrapper.subcategoria_Xcategoria(self.cod_category)
        self.cod_tipo_inmueble = list(pDF_subcat_inmuebles[pDF_subcat_inmuebles.name == tipo_inmueble]['id'])[0] #String
        pDF_tipos_operacion = self.data_scrapper.subcategoria_Xcategoria(self.cod_tipo_inmueble)
        lst_tipos_operacion = list(pDF_tipos_operacion['name'])
        return lst_tipos_operacion

    ## Funcion que pide a la capa de datos listado de 'Provincias', 
    # y devuelve listado a la capa de presentacion
    def get_provincias(self, pais):
        pDF_countries = self.data_scrapper.paises()
        self.cod_country = list(pDF_countries[pDF_countries.name == pais]['id'])[0] #String
        pDF_states = self.data_scrapper.estados_Xpais(self.cod_country)
        lst_states = list(pDF_states['name'])
        return lst_states

    ## Funcion que recibe la provincia seleccionada y pide a la capa de datos 
    # listado de 'Ciudades' y devuelve listado a la capa de presentacion
    def get_ciudades(self, provincia):
        pDF_states = self.data_scrapper.estados_Xpais(self.cod_country)
        self.cod_state = list(pDF_states[pDF_states.name == provincia]['id'])[0] #String
        pDF_cities = self.data_scrapper.ciudades_Xestado(self.cod_state)
        lst_cities = list(pDF_cities['name'])
        return lst_cities

    ## Funcion que recibe la ciudad seleccionada y pide a la capa de datos 
    # listado de 'Barrios' y devuelve listado a la capa de presentacion
    def get_barrios(self, ciudad):
        pDF_cities = self.data_scrapper.ciudades_Xestado(self.cod_state)
        self.cod_city = list(pDF_cities[pDF_cities.name == ciudad]['id'])[0] #String
        pDF_neighborhoods = self.data_scrapper.barrios_Xciudad(self.cod_city)
        if not pDF_neighborhoods.empty:
            lst_neighborhoods = (list(pDF_neighborhoods['name']))
        else:
            lst_neighborhoods = []
        return lst_neighborhoods

    ### Funcion que recibe la categoria seleccionada y offset, y pide a la capa de datos
    # la pagina del listado de resultados
    def get_resultados_Xcategoria(self, cod_categoria_selected, cod_site='MLA', state_id_selected=None, 
                                         city_id_selected=None, neighborhood_id_selected=None):
        pagenator = round(self.data_scrapper.nros_resultados_Xcategoria(cod_categoria_selected, cod_site)/50)
        pDF_list_inmuebles_Xubicacion = pandas.DataFrame()
        ########################################
        ### LIMITAMOS paginators para testeo ###
        if pagenator > 20: pagenator = 20
        ########################################
        ########################################
        ### Iteracion para recorrer todas las paginas de resultados
        for i in range(0,pagenator):
            offset = i * 50
            pDF_list_results = self.data_scrapper.resultados_Xcategoria(cod_categoria_selected, cod_site, offset)
            pDF_list_inmuebles_Xubicacion = pDF_list_inmuebles_Xubicacion.append(
                self.resultados_inmuebles_Xubicacion(pDF_list_results, state_id_selected, 
                city_id_selected, neighborhood_id_selected), ignore_index=True)  
        return pDF_list_inmuebles_Xubicacion
  
    ## Funcion que recibe pDF_list_results de la categoria INMUEBLES, y Estado, Ciudad, y/o Barrio 
    # seleccionados y devuelve pDF "id" publicacion, "site_id", "title" publicacion, "price", 
    # "currency_id", "condition", "permalink" publicacion, "category_id", 'latitude', 'longitude', 
    # 'address_line', 'zip_code', 'state_name', 'state_id', 'city_name', 'city_id',
    # 'neighborhood_name', 'neighborhood_id', 'sup_total', 'sup_total_unit', 'sup_cubierta',
    # 'sup_cubierta_unit', 'property_type'
    def resultados_inmuebles_Xubicacion (self, pDF_list_results_inmuebles, state_id_selected=None, 
                                         city_id_selected=None, neighborhood_id_selected=None):
        if not pDF_list_results_inmuebles.empty:
            # Convertimos datos 'location' en pDF
            list_locations = list(pDF_list_results_inmuebles['location'])
            pDF_list_locations = pandas.DataFrame(list_locations)
            # Convertimos datos anidados 'location' en pDF
            list_neighborhoods = list(pDF_list_locations['neighborhood'])
            pDF_list_neighborhoods = pandas.DataFrame(list_neighborhoods)
            list_cities = list(pDF_list_locations['city'])
            pDF_list_cities = pandas.DataFrame(list_cities)
            list_states = list(pDF_list_locations['state'])
            pDF_list_states = pandas.DataFrame(list_states)
            # Eliminamos columnas no necesarias del pDF
            # pDF_list_results = pDF_list_results_inmuebles[["id", "site_id", "title", "price", "currency_id", "condition", "permalink", "category_id", "attributes"]]       
            pDF_list_results = pDF_list_results_inmuebles.reindex(columns=["id", "site_id", "title", "price", "currency_id", "condition", "permalink", "category_id", "attributes"])       
            # Agregamos columnas con los datos desanidados
            pDF_list_results.loc[:,'latitude'] = list(pDF_list_locations.loc[:,'latitude'])
            pDF_list_results.loc[:,'longitude'] = list(pDF_list_locations.loc[:,'longitude'])
            pDF_list_results.loc[:,'address_line'] = list(pDF_list_locations.loc[:,'address_line'])
            pDF_list_results.loc[:,'zip_code'] = list(pDF_list_locations.loc[:,'zip_code'])
            pDF_list_results.loc[:,'state_name'] = list(pDF_list_states.loc[:,'name'])
            pDF_list_results.loc[:,'state_id'] = list(pDF_list_states.loc[:,'id'])
            pDF_list_results.loc[:,'city_name'] = list(pDF_list_cities.loc[:,'name'])
            pDF_list_results.loc[:,'city_id'] = list(pDF_list_cities.loc[:,'id'])
            pDF_list_results.loc[:,'neighborhood_name'] = list(pDF_list_neighborhoods.loc[:,'name'])
            pDF_list_results.loc[:,'neighborhood_id'] = list(pDF_list_neighborhoods.loc[:,'id'])
            # Filtramos la pagina de resultados por la ubicacion de mas precision seleccionada
            if neighborhood_id_selected != None:
                pDF_list_results2 = pDF_list_results[pDF_list_results.neighborhood_id == neighborhood_id_selected].reset_index(drop=True)
            elif city_id_selected != None:
                pDF_list_results2 = pDF_list_results[pDF_list_results.city_id == city_id_selected].reset_index(drop=True)
            elif state_id_selected != None:
                pDF_list_results2 = pDF_list_results[pDF_list_results.state_id == state_id_selected].reset_index(drop=True)
            # Convertimos los datos de atributos en diccionarios e inicializamos listas
            rows = pDF_list_results2.shape[0]
            pDF_attributes = pDF_list_results2.loc[:,'attributes']
            lst_sup_total = []
            lst_sup_total_unit = []
            lst_sup_cubierta = []
            lst_sup_cubierta_unit = []
            lst_prop_type = []
            # Iteracion para recorrer los datos de los atributos y extraer superficies
            for i in range(0, rows):
                lst_attributes = list(pDF_attributes.iloc[i])
                lst_sup_cubierta.append(0)
                lst_sup_cubierta_unit.append('')
                lst_sup_total.append(0)
                lst_sup_total_unit.append('')
                lst_prop_type.append('')
                for j in range(0, len(lst_attributes)):
                    if lst_attributes[j]['id'] in ("COVERED_AREA", "MAX_COVERED_AREA"):
                        lst_sup_cubierta[i] = lst_attributes[j]['value_struct']['number']
                        lst_sup_cubierta_unit[i] = lst_attributes[j]['value_struct']['unit']
                    elif lst_attributes[j]['id'] in ("TOTAL_AREA", "MAX_TOTAL_AREA"):
                        lst_sup_total[i] = lst_attributes[j]['value_struct']['number']
                        lst_sup_total_unit[i] = lst_attributes[j]['value_struct']['unit']
                    elif lst_attributes[j]['id'] == "PROPERTY_TYPE":
                        lst_prop_type[i] = lst_attributes[j]['value_name']
            # Agregamos como columnas los datos de superficie extraidos de los atributos
            pDF_list_results2.loc[:,'sup_total'] = lst_sup_total
            pDF_list_results2.loc[:,'sup_total_unit'] = lst_sup_total_unit
            pDF_list_results2.loc[:,'sup_cubierta'] = lst_sup_cubierta
            pDF_list_results2.loc[:,'sup_cubierta_unit'] = lst_sup_cubierta_unit
            pDF_list_results2.loc[:,'property_type'] = lst_prop_type
        else:
            pDF_list_results2 = pDF_list_results_inmuebles
        # Devolvemos los resultados de la pagina para agregarlos a los de las paginas anteriores
        return pDF_list_results2

    ## Funcion que recibe seleccion y usa funciones del data_modeler para 
    # generar pDF con el listado de inmuebles según selección. 
    # Luego envía los datos al mapper para generar el mapa con los inmuebles selecionados
    def generate_map(self, seleccion):
        ## Busca codigos de la seleccion
        pDF_sites = self.data_scrapper.sites()
        self.cod_site = list(pDF_sites[pDF_sites.name == 'Argentina']['id'])[0] #String
        pDF_categories = self.data_scrapper.categorias_Xsite(self.cod_site)
        self.cod_category = list(pDF_categories[pDF_categories.name == 'Inmuebles']['id'])[0] #String
        pDF_subcat_inmuebles = self.data_scrapper.subcategoria_Xcategoria(self.cod_category)
        self.cod_tipo_inmueble = list(pDF_subcat_inmuebles[pDF_subcat_inmuebles.name == seleccion[0]]['id'])[0] #String
        pDF_tipos_operacion = self.data_scrapper.subcategoria_Xcategoria(self.cod_tipo_inmueble)
        self.cod_subcat_operacion = list(pDF_tipos_operacion[pDF_tipos_operacion.name == seleccion[1]]['id'])[0] #String
        pDF_countries = self.data_scrapper.paises()
        self.cod_country = list(pDF_countries[pDF_countries.name == 'Argentina']['id'])[0] #String
        pDF_states = self.data_scrapper.estados_Xpais(self.cod_country)
        self.cod_state = list(pDF_states[pDF_states.name == seleccion[2]]['id'])[0] #String
        try: 
            pDF_cities = self.data_scrapper.ciudades_Xestado(self.cod_state)
            self.cod_city = list(pDF_cities[pDF_cities.name == seleccion[3]]['id'])[0] #String
        except:
            self.cod_city = None
        try:
            pDF_neighborhoods = self.data_scrapper.barrios_Xciudad(self.cod_city)
            self.cod_neigborhood = list(pDF_neighborhoods[pDF_neighborhoods.name == seleccion[4]]['id'])[0] #String
        except:
            self.cod_neigborhood = None
        # Se solicita el listado de inmuebles según selección 
        pDF_inmuebles_seleccion = self.get_resultados_Xcategoria(self.cod_subcat_operacion, 
                                                                cod_site='MLA', 
                                                                state_id_selected=self.cod_state,
                                                                city_id_selected=self.cod_city, 
                                                                neighborhood_id_selected=self.cod_neigborhood)
        # Aplicamos la 1ra Regla de Negocios para eliminar OUTLIERS
        pDF_inmuebles_sin_outliers = self.get_rid_outliers(pDF_inmuebles_seleccion)
        # Aplicamos la 2da Regla de Negocios para codificar los marcadores segun
        # precio del metro cuadrado (en dolares)
        pDF_inmuebles_colores = self.get_markers_colors(pDF_inmuebles_sin_outliers)
        # Aplicamos al 3ra Regla de Negocios para extraer la informacion para mapear 
        pDF_inmuebles_mapear = self.text_popup(pDF_inmuebles_colores)[["latitude", "longitude", "text_popup", "color_marker"]]

        # Segun la precision de la seleccion se buscan las coordenadas y se determina zoom inicial
        if self.cod_neigborhood !=None:
            coordinates_map = self.data_scrapper.coordenadas_Xbarrio(self.cod_neigborhood)
            zoom_level = 15
        elif self.cod_city !=None:
            coordinates_map = self.data_scrapper.coordenadas_Xciudad(self.cod_city)
            zoom_level = 13
        else: 
            coordinates_map = self.data_scrapper.coordenadas_Xestado(self.cod_state)
            zoom_level = 7

        # Solicitamos al modulo 'mapper' que cree el objeto MAPA
        mapa = mapper.map_create(coordinates_map['latitude'], 
                                 coordinates_map['longitude'],
                                 zoom_level, 'OpenStreetMap')
        # Solicitamos al modulo 'mapper' que cree los marcadores
        mapa = mapper.markers_add(mapa, pDF_inmuebles_mapear)
        # Solicitamos al modulo 'mapper' que guarde el mapa en html
        mapper.map_save(mapa)
        return     

    ## Funcion que recibe pDF con listado de inmuebles seleccionados y filtra 
    # los inmuebles con precios del metro cuadrado por debajo 
    # del 10% del precio metro cuadrado promedio, y los inmuebles 
    # con precios del metro cuadrado mayores a 10 veces el precio 
    # del metro cuadrado promedio, elimina items sin los datos necesarios para el mapeo
    def get_rid_outliers(self, pDF_inmuebles_seleccion):
        try:
            dollar = geeklab_dollarAPI.get_dollar()
        except: 
            dollar = 58.5
        pDF_inmuebles_seleccion0 = pDF_inmuebles_seleccion[pDF_inmuebles_seleccion.latitude.notnull()].reset_index(drop=True)
        pDF_inmuebles_seleccion1 = pDF_inmuebles_seleccion0[pDF_inmuebles_seleccion0.price.notnull()].reset_index(drop=True)
        pDF_inmuebles_seleccion2 = pDF_inmuebles_seleccion1[pDF_inmuebles_seleccion1.price != 0].reset_index(drop=True)        
        # pDF_inmuebles_seleccion3 = pDF_inmuebles_seleccion2[pDF_inmuebles_seleccion2.price != ''].reset_index(drop=True)                
        # FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
        rows = pDF_inmuebles_seleccion2.shape[0]
        pDF_inmuebles_seleccion2['priceUSD'] = 0.0
        pDF_inmuebles_seleccion2['sup_total_mts'] = 0.0
        pDF_inmuebles_seleccion2['sup_cubierta_mts'] = 0.0
        for i in range(0, rows):
            if pDF_inmuebles_seleccion2.iloc[i]['currency_id'] == 'USD':
                pDF_inmuebles_seleccion2.at[i, 'priceUSD'] = float(pDF_inmuebles_seleccion2.iloc[i]['price'])
            elif pDF_inmuebles_seleccion2.iloc[i]['currency_id'] == 'ARS':
                pDF_inmuebles_seleccion2.at[i, 'priceUSD'] = float(pDF_inmuebles_seleccion2.iloc[i]['price'])/dollar
            if pDF_inmuebles_seleccion2.iloc[i]['sup_total_unit'] == 'ha':
                pDF_inmuebles_seleccion2.at[i, 'sup_total_mts'] = (pDF_inmuebles_seleccion2.iloc[i]['sup_total']*10000)
            else:
                pDF_inmuebles_seleccion2.at[i, 'sup_total_mts'] = (pDF_inmuebles_seleccion2.iloc[i]['sup_total'])
            if pDF_inmuebles_seleccion2.iloc[i]['sup_cubierta_unit'] == 'ha':
                pDF_inmuebles_seleccion2.at[i, 'sup_cubierta_mts'] = (pDF_inmuebles_seleccion2.iloc[i]['sup_cubierta']*10000)
            else:
                pDF_inmuebles_seleccion2.at[i, 'sup_cubierta_mts'] = (pDF_inmuebles_seleccion2.iloc[i]['sup_cubierta'])

        pDF_inmuebles_seleccion4 = pDF_inmuebles_seleccion2[pDF_inmuebles_seleccion2.priceUSD != 0].reset_index(drop=True)
        rows = pDF_inmuebles_seleccion4.shape[0]
        pDF_inmuebles_seleccion4['priceUSD_Xm2'] = 0.0
        for i in range(0, rows):
            if pDF_inmuebles_seleccion4.iloc[i]['property_type']in('Campos', 'Terrenos y Lotes'):
                if pDF_inmuebles_seleccion4.iloc[i]['sup_total_mts']!=0:
                    pDF_inmuebles_seleccion4.at[i, 'priceUSD_Xm2'] = (float(pDF_inmuebles_seleccion4.iloc[i]['priceUSD']) 
                    / float(pDF_inmuebles_seleccion4.iloc[i]['sup_total_mts']))
                else: 
                    pDF_inmuebles_seleccion4.at[i, 'priceUSD_Xm2'] = 0
            elif pDF_inmuebles_seleccion4.iloc[i]['property_type']in('Camas Náuticas', 'Parcelas, Nichos y Bóvedas'):
                pDF_inmuebles_seleccion4.at[i, 'priceUSD_Xm2'] = ''
            else:
                if pDF_inmuebles_seleccion4.iloc[i]['sup_cubierta_mts']!=0:
                    pDF_inmuebles_seleccion4.at[i, 'priceUSD_Xm2'] = (float(pDF_inmuebles_seleccion4.iloc[i]['priceUSD']) 
                    / float(pDF_inmuebles_seleccion4.iloc[i]['sup_cubierta_mts']))
                else:
                    pDF_inmuebles_seleccion4.at[i, 'priceUSD_Xm2'] = 0
        try: 
            priceUSD_avg_Xm2 = pDF_inmuebles_seleccion4['priceUSD_Xm2'].mean()
            pDF_inmuebles_seleccion5 = pDF_inmuebles_seleccion4[pDF_inmuebles_seleccion4.priceUSD_Xm2 > (priceUSD_avg_Xm2*0.1)].reset_index(drop=True)
            pDF_inmuebles_seleccion6 = pDF_inmuebles_seleccion5[pDF_inmuebles_seleccion5.priceUSD_Xm2 < (priceUSD_avg_Xm2*10)].reset_index(drop=True)
            pDF_inmuebles_sin_outliers = pDF_inmuebles_seleccion6
        except:
            pDF_inmuebles_sin_outliers = pDF_inmuebles_seleccion4.reset_index(drop=True)
        return pDF_inmuebles_sin_outliers


    ## Funcion que pDF inmuebles sin outliers y devuelve
    # pDF inmuebles con columna color marcadores segun precio promedio m2
    def get_markers_colors(self, pDF_inmuebles_sin_colores):
        pDF_inmuebles_sin_colores['color_marker'] = 'green'
        try: 
            priceUSD_max_Xm2 = pDF_inmuebles_sin_colores['priceUSD_Xm2'].max()
            priceUSD_min_Xm2 = pDF_inmuebles_sin_colores['priceUSD_Xm2'].min()
            rows = pDF_inmuebles_sin_colores.shape[0]
            for i in range(0, rows):
                pDF_inmuebles_sin_colores.at[i, 'color_marker'] = mapper.marker_color(
                    pDF_inmuebles_sin_colores.iloc[i]['priceUSD_Xm2'], 
                    priceUSD_min_Xm2, 
                    priceUSD_max_Xm2)
            pDF_inmuebles_colores = pDF_inmuebles_sin_colores
        except:
            pDF_inmuebles_colores = pDF_inmuebles_sin_colores
        return pDF_inmuebles_colores

    ## Funcion que recibe pDF con inmuebles y devuelve pDF con columna
    # texto popup para los marcadores
    def text_popup(self, pDF_inmuebles_colores):
        rows = pDF_inmuebles_colores.shape[0]
        pDF_inmuebles_colores['text_popup'] = ''
        locale.setlocale(locale.LC_NUMERIC, 'es_AR.UTF8')
        for i in range(0, rows):
            pDF_inmuebles_colores.at[i, 'text_popup'] = (
                str(pDF_inmuebles_colores.iloc[i]['title']) + ' <br>' +\
                'Precio: ' + str(pDF_inmuebles_colores.iloc[i]['currency_id']) + ' ' + str(locale.format_string('%.2f', pDF_inmuebles_colores.iloc[i]['price'], True)) + ' <br>' +\
                'PrecioXm2 (USD): ' + str(locale.format_string('%.2f', pDF_inmuebles_colores.iloc[i]['priceUSD_Xm2'], True)) + ' <br>' +\
                'Sup.Total (m2): ' + str(locale.format_string('%.2f', pDF_inmuebles_colores.iloc[i]['sup_total_mts'], True)) + ' <br>' +\
                'Sup.Cubierta (m2): ' + str(locale.format_string('%.2f', pDF_inmuebles_colores.iloc[i]['sup_cubierta_mts'], True)) + ' <br>' +\
                'Link: ' + str(pDF_inmuebles_colores.iloc[i]['permalink']))
                # locale.format_string('%.2f', 12345.6789, True)
        pDF_inmuebles_mapear = pDF_inmuebles_colores
        return pDF_inmuebles_mapear

    
if __name__ == "__main__":
    pass


### "id": "MLA1459", "name": "Inmuebles"
### "id": "MLA1472", "name": "Departamentos"
### "id": "MLA1473", "name": "Departamentos/Alquiler"
### "id": "MLA1496", "name": "Campos"
### "id": "MLA6414", "name": "Campos/Alquiler"
## TUxBUFNBTmU5Nzk2                Santa Fe
## TUxBQ1JPUzg1Yjg3                Rosario
## TUxBQlJPUzI5MDha                Centro

# id: "MLA374730"	"name": "Camas NÃ¡uticas"       "total_items_in_this_category": 352
# id: "MLA50544"	"name": "Parcelas	            "total_items_in_this_category": 428		
		
# id: "MLA1496"	    "name": "Campos"	            "total_items_in_this_category": 4686    "id": "TOTAL_AREA"

# id: "MLA50541"	"name": "Cocheras"	            "total_items_in_this_category": 8514    "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	
# id: "MLA392265"	"name": "Consultorios"	        "total_items_in_this_category": 561     "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	
# id: "MLA1475"	    "name": "DepÃ³sitos y Galpones" "total_items_in_this_category": 11574   "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	
# id: "MLA50545"	"name": "Fondo de Comercio"	    "total_items_in_this_category": 3515    "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	
# id: "MLA79242"	"name": "Locales"	            "total_items_in_this_category": 19863   "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	
# id: "MLA50538"	"name": "Oficinas"	            "total_items_in_this_category": 14347   "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	
# id: "MLA105179"	"name": "PH"	                "total_items_in_this_category": 18714   "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	
# id: "MLA50547"	"name": "Quintas"	            "total_items_in_this_category": 4276    "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	
# id: "MLA50536"	"name": "Tiempo Compartido"	    "total_items_in_this_category": 550     "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	
# id: "MLA1892"	    "name": "Otros Inmuebles"	    "total_items_in_this_category": 4342    "id": "TOTAL_AREA"	    "id": "COVERED_AREA"	

# id: "MLA1466"	    "name": "Casas"	                "total_items_in_this_category": 135682  "id": "MAX_TOTAL_AREA"  "id": "MAX_COVERED_AREA"    "id": "MIN_COVERED_AREA"
# id: "MLA1493"	    "name": "Terrenos y Lotes"	    "total_items_in_this_category": 82998   "id": "MAX_TOTAL_AREA"	"id": "MAX_COVERED_AREA"    "id": "MIN_COVERED_AREA"
# id: "MLA1472"	    "name": "Departamentos"	        "total_items_in_this_category": 202957  "id": "MAX_TOTAL_AREA"	"id": "MAX_COVERED_AREA"    "id": "MIN_COVERED_AREA"
