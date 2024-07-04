from app_parcial import *
from parcialfunciones import *
from ejercicios import *
import os
lista_bicicletas = []
flag_archivo = False
while True:
    limpiar_pantalla()
    match menu():
        case "1":
            nombre_archivo = input("ingrese el nombre del archivo .CSV a cargar: ")
            cargar_archivo_csv(nombre_archivo,lista_bicicletas)
            flag_archivo = True
            print("Archivo cargardo con exito!")
        case "2":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    mostrar_ciclistas_tabla(cargar_archivo_csv("bicicletas.csv",lista_bicicletas))
                except:
                    raise ValueError("ese archivo no existe")
        case "3":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    lista_tiempos_random = cargar_datos_random(lista,"tiempo")
                    mostrar_ciclistas_tabla(lista_tiempos_random)
                except:
                    raise ValueError("No hay un archivo cargado")
        case "4":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    ganadores()
                except:
                    raise ValueError("No hay un archivo cargado")
                
        case "5":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    crear_archivo_tipo_csv(lista_tiempos_random)
                except:
                    raise ValueError("No hay un archivo cargado")
                
        case "6":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    promedio_tipo()
                except:
                    raise ValueError("No hay un archivo cargado")
                
        case "7":
            if flag_archivo == False:
                print("no hay archivo cargado")
            else:
                try:
                    ordenar_lista_doble(lista_tiempos_random,"tipo","tiempo")
                    mostrar_ciclistas_tabla(lista_tiempos_random)
                except:
                    raise ValueError("No hay un archivo cargado")

        case "8":
            if flag_archivo == False:
                print("no hay archivo cargado")
            else:
                try:
                    crear_archivo_json(lista_tiempos_random)
                except:
                    raise ValueError("No hay un archivo cargado")
            
        case "9":
            if salir() == "no":
                menu()
            else:
                break

    pausar()

