import pandas
import folium


## funcion para crear mapa con folium
def map_create(center_map_latitude, center_map_longitude, 
                initial_zoom, tiles_type):
    map_created = folium.Map(location=[center_map_latitude, center_map_longitude], 
                             zoom_start=initial_zoom, 
                             tiles=tiles_type)
    return map_created


## funcion para agregar marcadores recibe 'nombre_mapa'
# pDF con listado de inmuebles y las columnas necesarias para crear marcadores
# latitud, longitud, text_popup, color_marker
def markers_add(map_created, panda_dataframe, max_width_popup=300, min_width_popup=300, icon_type='marker'):
    ## itera por cada fila del DataFrame
    for i in range(0, panda_dataframe.shape[0]):
        ## crea un marcador item
        folium.Marker(location=[panda_dataframe.iloc[i]['latitude'], panda_dataframe.iloc[i]['longitude']], 
                      popup=folium.Popup(panda_dataframe.iloc[i]['text_popup'], 
                                         max_width=max_width_popup,
                                         min_width=min_width_popup), 
                      icon=folium.Icon(icon = icon_type, 
                                       color = panda_dataframe.iloc[i]['color_marker'])
                     ).add_to(map_created)
    return map_created


## funcion para guardar mapa en html
def map_save(map_created):
    map_created.save('map_created.html')


## define funcion para determinar color del marcador
def marker_color(value, min_value, max_value):
    step = (max_value - min_value) / 3
    ## asigna color segun valor
    if int(value) in range (int(min_value), int(min_value + step)):
        icon_color = 'green'
    elif int(value) in range (int(min_value + step), int(min_value + step*2)):
        icon_color = 'orange'
    else:
        icon_color = 'red'
    return icon_color

