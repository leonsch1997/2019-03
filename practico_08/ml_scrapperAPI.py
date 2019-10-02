import pandas
import requests
import json


class ML_API:
    ## Funcion que recibe codigo site y pide a la API de ML
    # datos categorias y devuelve pDF "id", "name" de categorias
    def categorias_Xsite (self, cod_site):
        ml_url_get_categories = 'https://api.mercadolibre.com/sites/{0}/categories'.format(cod_site)
        pDF_list_categories = pandas.read_json(ml_url_get_categories)
        return pDF_list_categories

    ## Funcion que pide a la API de ML datos de sites
    # y devuelve pDF  "default_currency_id", "id", "name" de sites
    def sites (self):
        ml_url_get_sites = 'https://api.mercadolibre.com/sites'
        pDF_list_sites = pandas.read_json(ml_url_get_sites)
        return pDF_list_sites 

    ## Funcion que pide a la API de ML datos de paises
    # y devuelve pDF  "id", "name", "locale", "currency_id" de paises
    def paises (self):
        ml_url_get_countries = 'https://api.mercadolibre.com/classified_locations/countries'
        pDF_list_countries = pandas.read_json(ml_url_get_countries)
        return pDF_list_countries    

    ## Funcion que recibe codigo pais y pide a la API de ML
    # datos pais y devuelve pDF "id", "name" estados
    def estados_Xpais (self, cod_pais):
        ml_url_get_country = 'https://api.mercadolibre.com/classified_locations/countries/{0}'.format(cod_pais)
        pDF_mljson_country = pandas.read_json(ml_url_get_country, orient='index')
        list_states = pandas.DataFrame(pDF_mljson_country.loc['states']).loc[0]['states']
        pDF_list_states = pandas.DataFrame(list_states)
        return pDF_list_states

    ## Funcion que recibe codigo estado y pide a la API de ML
    # datos estado y devuelve pDF "id", "name" ciudades
    def ciudades_Xestado (self, cod_estado):
        ml_url_get_state = 'https://api.mercadolibre.com/classified_locations/states/{0}'.format(cod_estado)
        pDF_mljson_state = pandas.read_json(ml_url_get_state, orient='index')
        list_cities = pandas.DataFrame(pDF_mljson_state.loc['cities']).loc[0]['cities']
        pDF_list_cities = pandas.DataFrame(list_cities)
        return pDF_list_cities

    ## Funcion que recibe codigo ciudad y pide a la API de ML
    # datos ciudad y devuelve pDF "id", "name" barrios
    def barrios_Xciudad (self, cod_ciudad):
        try: 
            ml_url_get_city = 'https://api.mercadolibre.com/classified_locations/cities/{0}'.format(cod_ciudad)
            pDF_mljson_city = pandas.read_json(ml_url_get_city, orient='index')
            list_neighborhoods = pandas.DataFrame(pDF_mljson_city.loc['neighborhoods']).loc[0]['neighborhoods']
            pDF_list_neighborhoods = pandas.DataFrame(list_neighborhoods)
        except:
            pDF_list_neighborhoods = pandas.DataFrame([])
        return pDF_list_neighborhoods

    ## Funcion que recibe codigo de estado y devuelve sus coordenadas segun API Mercado Libre
    def coordenadas_Xestado(self, cod_estado):
        ml_url_get_state = 'https://api.mercadolibre.com/classified_locations/states/{0}'.format(cod_estado)
        pDF_mljson_state = pandas.read_json(ml_url_get_state, orient='index')
        dict_state_coordinates = (list(pDF_mljson_state.loc['geo_information']))[0]['location']
        return dict_state_coordinates

    ## Funcion que recibe codigo de ciudad y devuelve sus coordenadas segun API Mercado Libre
    def coordenadas_Xciudad(self, cod_ciudad):
        ml_url_get_city = 'https://api.mercadolibre.com/classified_locations/cities/{0}'.format(cod_ciudad)
        pDF_mljson_city = pandas.read_json(ml_url_get_city, orient='index')
        dict_city_coordinates = (list(pDF_mljson_city.loc['geo_information']))[0]['location']
        return dict_city_coordinates
    
    ## Funcion que recibe codigo de barrio y devuelve sus coordenadas segun API Mercado Libre
    def coordenadas_Xbarrio(self, cod_barrio):
        ml_url_get_neighborhoods = 'https://api.mercadolibre.com/classified_locations/neighborhoods/{0}'.format(cod_barrio)
        pDF_mljson_neighborhoods = pandas.read_json(ml_url_get_neighborhoods, orient='index')
        dict_neighborhoods_coordinates = (list(pDF_mljson_neighborhoods.loc['geo_information']))[0]['location']
        return dict_neighborhoods_coordinates

    ## Funcion que recibe codigo categoria y pide a la API de ML
    # datos categoria y devuelve pDF "id", "name", "total_items_in_this_category" de subcategorias
    def subcategoria_Xcategoria (self, cod_categoria):
        ml_url_get_category = 'https://api.mercadolibre.com/categories/{0}'.format(cod_categoria)
        pDF_mljson_category = pandas.read_json(ml_url_get_category, orient='index')
        list_children_categories = pandas.DataFrame(pDF_mljson_category.loc['children_categories']).loc[0]['children_categories']
        pDF_list_children_categories = pandas.DataFrame(list_children_categories)
        return pDF_list_children_categories

    ## Funcion que recibe codigo categoria, el código de site, el offset,
    # pide a la API una pagina de los items listados y devuelve pDF con los resultados
    def resultados_Xcategoria (self, cod_categoria, cod_site, offset):
        ml_url_get_results = 'https://api.mercadolibre.com/sites/{1}/search?category={0}&limit=50&offset={2}'.format(cod_categoria, cod_site, offset)
        pDF_mljson_results = pandas.read_json(ml_url_get_results, orient='index')
        list_results = pandas.DataFrame(pDF_mljson_results.loc['results']).loc[0]['results']
        pDF_list_results = pandas.DataFrame(list_results)
        return pDF_list_results
    
    ## Funcion que recibe codigo categoria, el código de site, el offset,
    # pide a la API una pagina de los items listados y devuelve pDF con los resultados
    def nros_resultados_Xcategoria (self, cod_categoria, cod_site):
        ml_url_get_results = 'https://api.mercadolibre.com/sites/{1}/search?category={0}'.format(cod_categoria, cod_site)
        nro_resultados = list(pandas.read_json(ml_url_get_results, orient='index').loc['paging'])[0]['total'] #Integer
        return nro_resultados


if __name__ == "__main__":
    pass