from parcialfunciones import *
from random import *

# 1. Cargar archivo .CSV

def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

with open(get_path_actual("bicicletas.csv"), "r", encoding="utf-8") as archivo :
    lista_bicicletas = []
    encabezado = archivo.readline().strip("\n").split(",")

    for linea in archivo.readlines():
        bicicleta= {}
        linea = linea.strip("\n").split(",")

        id_bike, nombre, tipo, tiempo = linea
        bicicleta["id_bike"] = int(id_bike)
        bicicleta["nombre"] = nombre
        bicicleta["tipo"] = tipo
        bicicleta["tiempo"] = int(tiempo)
        
        lista_bicicletas.append(bicicleta)



for bicicleta in lista_bicicletas:
    print(bicicleta)


#2. Imprimir lista 

print(lista_bicicletas)

#3

lista_tiempos = mapear_lista(lambda time : time["tiempo"],lista_bicicletas)




for bici in range(len(lista_tiempos)):
    time_value= randint(50,120)
    lista_bicicletas[bici]["tiempo"] = lista_bicicletas[bici]["tiempo"] = time_value

print(f"Lista tiempos actualizada: \n  {lista_bicicletas}")


#4

ganador = calcular_menor_campo_nombre(lista_bicicletas,"tiempo","nombre")
tiempo = calcular_menor_campo_nombre(lista_bicicletas,"tiempo","tiempo")



print(f"el ganador es... {ganador} {tiempo}s")

#5

#5
def enlistar(lista,campo1,campo_agrupado)->dict:
    #mapear lista previamente
    campo = {}
    for el in lista:
        campo[el] = ""

    for i in lista_bicicletas: #la lista cambia en base a la data.
        for j in campo.keys():
            if i[campo1] == j:
                campo[j] += f"{i[campo_agrupado]} , "

    return campo

tipos_bicicleta= mapear_lista(lambda tipo: tipo["tipo"] , filtrar_lista(lambda tipos: tipos["tipo"] == "BMX" , lista_bicicletas))

lista_bici = enlistar(tipos_bicicleta,"tipo","nombre")
print(lista_bici)


with open(get_path_actual("bicicletas_tipo.csv"), "w", encoding="utf-8") as archivo :
    encabezado = ",".join(list(lista_bicicletas[0].keys())) + "\n"
    archivo.write(encabezado)
    for bicicleta in lista_bicicletas:
        values = list(bicicleta.values())
        l = []
        for value in values:
            if isinstance(value, int): 
                l.append(str(value))
            elif isinstance(value, float): 
                l.append(str(value))
            else:
                l.append(value)
        linea = ",".join(l) + "\n"
        archivo.write(linea)

#  
#bici_mapeo = mapear_lista(lambda tipo: tipo["tiempo"],lista_bicicletas)

#print(bici_mapeo)







print( "             PROMEDIOS ")


filtro_bmx = filtrar_lista(lambda bici : bici["tipo"] == "BMX",lista_bicicletas)

promedio_bmx = promediar_coleccion(filtro_bmx,"tiempo")

print(F"BMX: \n {promedio_bmx}")

filtro_paseo= filtrar_lista(lambda bici : bici["tipo"] == "PASEO",lista_bicicletas)

promedio_paseo = promediar_coleccion(filtro_paseo,"tiempo")

print(F"PASEO: \n {promedio_paseo}")

filtro_playera = filtrar_lista(lambda bici : bici["tipo"] == "PLAYERA",lista_bicicletas)

promedio_playera = promediar_coleccion(filtro_playera,"tiempo")

print(F"PLAYERA: \n {promedio_playera}")

filtro_mtb = filtrar_lista(lambda bici : bici["tipo"] == "MTB",lista_bicicletas)

promedio_mtb = promediar_coleccion(filtro_mtb,"tiempo")

print(F"MTB: \n {promedio_mtb}")

