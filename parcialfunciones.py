from random import *

def calcular_mayor_campo(lista,campo):
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    maximo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) > float(maximo[campo]):
            maximo = diccionarios
            
    return maximo

def calcular_menor_campo(lista,campo)->float:
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    maximo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) < float((maximo[campo])):
            maximo = diccionarios
            
    return maximo


def filtrar_superheroes(lista,altura):
    lista_retorno = []
    for el in lista:
        if el["altura"] == altura:
            lista_retorno.append(el)
    return lista_retorno


def lista_campo(lista,campo):
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el[campo]))
    return lista_retorno


def filtrar_superheroes(lista, nombre,altura):
    lista_retorno = []
    for el in lista:
        if el["nombre"] == nombre:
            lista_retorno.append(el)
            if el["altura"] == altura:
                lista_retorno.append(el)
    return lista_retorno

def lista_nombre_altura(lista,nombre,altura):
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el[nombre]))
        lista_retorno.append((el[altura]))
    return lista_retorno

def promediar_coleccion(lista,campo): 
    """saca el promedio de una coleccion

    Args:
        lista (_type_): ingresa lista a promediar
        campo (_type_): ingresa campo a promediar

    Returns:
        _type_: devuelve el promedio del campo establecido en float
    """
    suma = 0
    total_iteraciones = 0
    for personaje in lista:
        total_iteraciones += 1
        suma += float(personaje[campo])
        

    return suma / total_iteraciones

def mapear_lista(funcion,lista):
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno


def filtrar_lista(funcion,lista): # GENERICA
    lista_retorno = []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno

def each_lista(funcion,lista): #  GENERICA
    for el in lista:
        funcion(el)

def reduce_lista(funcion, lista:list)->any :
    ant = lista[0]
    for el in lista[1:]:
        ant = funcion(ant, el)
    return ant

def calcular_mayor_campo_nombre(lista,campo,campo2): #campo 2 printea cualquier valor
    """Le asigna un valor al campo 1

    Args:
        lista (_type_): ingresa lista 
        campo (_type_): campo a comparar
        campo2 (_type_): valor a asociar al campo

    Raises:
        ValueError: _description_

    Returns:
        _type_: el nombre asociado al campo a comparar
    """
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    nombre_maximo = lista[0]
    maximo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) >= float(maximo[campo]):
            maximo = diccionarios
            nombre_maximo = diccionarios[campo2]
        
    return nombre_maximo

def calcular_menor_campo_nombre(lista,campo,campo2):
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    nombre_minimo = lista[0]
    minimo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) <= float(minimo[campo]):
            minimo = diccionarios
            nombre_minimo = diccionarios[campo2]
        
    return nombre_minimo

def contador_lista(lista,campo):
    campo = {}
    for el in lista:
        campo[el] = 0

    for el in lista:
        for i in campo:
            if el == i:
                campo[el] += 1

    return campo

def enlistar(lista,campo1,campo_agrupado)->dict:
    #mapear lista previamente
    campo = {}
    for el in lista:
        campo[el] = ""

    for i in lista: #la lista cambia en base a la data.
        for j in campo.keys():
            if i[campo1] == j:
                campo[j] += f"{i[campo_agrupado]} , "

    return campo

def randomizar(lista,campo):
    campo_lista = {}
    for i in lista:
        i[campo] += randint(50,120)

    return campo_lista

def promediar_coleccion(lista,campo): 
    """saca el promedio de una coleccion

    Args:
        lista (_type_): ingresa lista a promediar
        campo (_type_): ingresa campo a promediar

    Returns:
        _type_: devuelve el promedio del campo establecido en float
    """
    suma = 0
    total_iteraciones = 0
    for personaje in lista:
        total_iteraciones += 1
        suma += float(personaje[campo])
        promedio = suma / total_iteraciones

    return promedio

def calcular_promedio(lista:list)->float:
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("No esta definido el promedio de una lista vacia")
        return totalizar_lista(lista) / cant
    raise ValueError("Eso no es una lista") 

def definir_campo(campo):
    match campo:
        case "B":
            retorno = "BMX"
        case "M":
            retorno = "MTB"
        case "P":
            retorno = "PASEO"
        case "p":
            retorno = "PLAYERA"
    return retorno

def ordenar_bicis(lista,campo,asc:bool = True):
    atributo = definir_campo
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][atributo] > lista[j][atributo] if asc else lista[i][atributo] < lista[j][atributo]:
                swap_lista(lista,i,j)

def ordenar_lista_doble(lista, campo1, campo2):
    if isinstance(lista,list):
            atributo = definir_campo(campo1)
            atributo2 = definir_campo(campo2)
            tam = len(lista)
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i][atributo] == lista[j][atributo]:
                        if lista[i][atributo2] > lista[j][atributo2]:
                            swap_lista(lista, i, j)  
                    elif lista[i][atributo] > lista[j][atributo]:
                        swap_lista(lista,i,j)
    else:
        raise ValueError("No se ingreso ninguna lista")