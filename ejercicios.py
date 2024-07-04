from parcialfunciones import *
import random
import json 
# 1. Cargar archivo .CSV
lista_bicicletas =[]


def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def cargar_archivo_csv(nombre_archivo,lista):
    """ Carga un archivo .CSV

    Args:
        nombre_archivo (_type_): _description_
        lista (_type_): _description_

    Returns:
        _type_: me retorna el contenido del archivo en una lista.
    """
    with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo :
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")

        for linea in archivo.readlines():
            bicicleta= {}
            linea = linea.strip("\n").split(",")

            id_bike, nombre, tipo, tiempo = linea
            bicicleta["id_bike"] = int(id_bike)
            bicicleta["nombre"] = nombre
            bicicleta["tipo"] = tipo
            bicicleta["tiempo"] = int(tiempo)

            lista.append(bicicleta)
    return lista

#2 imprimir lista
lista = cargar_archivo_csv("bicicletas.csv",lista_bicicletas)


#3 asignar tiempos

def cargar_datos_random(lista,campo) -> list:
    """carga datos random a un campo ingresado.

    Args:
        lista (_type_): _description_
        campo (_type_): _description_

    Returns:
        list: _description_
    """
    lista_tiempos = mapear_lista(lambda tiempo : tiempo[campo],lista)
    for value in range(len(lista_tiempos)):
        lista_tiempos[value] = random.randint(50,120)
        lista[value][campo] = lista_tiempos[value]
    return lista
    




#4
def ganadores():
    """muestra el nombre del usuario ganador y sus tiempo
    """
    nombre_ganador = calcular_mayor_campo_nombre(lista,"tiempo","nombre")
    tiempo_ganador = calcular_menor_campo_nombre(lista,"tiempo","tiempo")
    print(f"{nombre_ganador} {tiempo_ganador}s")



#5

def crear_archivo_tipo_csv(lista:list):
    """crea un archivo de tipo .CSV filtrando por tipo.

    Args:
        lista (list): _description_
    """
    type_bike = input("Ingrese el tipo de bicicleta: ")
    while type_bike != "BMX" and type_bike != "PLAYERA" and type_bike != "MTB" and type_bike != "PASEO":
        type_bike = input("Ingrese un tipo de bicicleta valido: ")
    lista_tipo = (filtrar_lista(lambda bike: bike["tipo"] == type_bike, lista))
    
    with open(get_path_actual(type_bike + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista_tipo)):
            lista_cargada = ",".join(lista_tipo[i]) + "\n"

        for persona in lista_tipo:
            values = list(persona.values())
            lista_cargada = []
            for value in values:
                if isinstance(value,int):
                    lista_cargada.append(str(value))
                elif isinstance(value,float):
                    lista_cargada.append(str(value))
                else:
                    lista_cargada.append(value)
            linea = ",".join(lista_cargada) + "\n"
            archivo.write(linea)


#6
def promedio_tipo():
    """filtra las bicis por tipo y las promedia.
    """
    lista_bmx = filtrar_lista(lambda tipo: tipo["tipo"] == "BMX",lista)
    promedio_bmx = promediar_coleccion(lista_bmx,"tiempo")
    print(f"PROMEDIO BMX: \n {promedio_bmx:.2f}")

    lista_mtb = filtrar_lista(lambda tipo: tipo["tipo"] == "MTB",lista)
    promedio_mtb = promediar_coleccion(lista_mtb,"tiempo")
    print(f"PROMEDIO MTB: \n {promedio_mtb:.2f}")

    lista_playera = filtrar_lista(lambda tipo: tipo["tipo"] == "PLAYERA",lista)
    promedio_playera = promediar_coleccion(lista_playera,"tiempo")
    print(f"PROMEDIO PLAYERA: \n {promedio_playera:.2f}")

    lista_paseo = filtrar_lista(lambda tipo: tipo["tipo"] == "PASEO",lista)
    promedio_paseo = promediar_coleccion(lista_paseo,"tiempo")
    print(f"PROMEDIO PASEO: \n {promedio_paseo:.2f}")


#8
def crear_archivo_json(lista):
    """crea un archivo .JSON

    Args:
        lista (_type_): _description_
    """
    nombre_archivo = input("ingrese el nombre del archivo a asignar")
    with open(get_path_actual(nombre_archivo +".json"), "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo,indent = 2)
    

