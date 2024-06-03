from data_stark import *
import os


################################################## MENÚ #####################################################

def limpiar_pantalla():
    """Limpia la pantalla al volver al menú
    """
    os.system("cls")

def pausar():

    os.system("pause")

def menu():
    """Muestra un menú de opciones para Stark Industries
    """
    limpiar_pantalla()
    print("             Stark Industries")
    print("--------------------------------------------")
    print("1) Mostrar el nombre de los Superhéroes")
    print("2) Mostrar el nombre de los Superhéroes Masculinos")
    print("3) Mostrar el nombre de los Superhéroes Femeninos")
    print("4) Mostrar nombre y altura de los Superhéroes")
    print("5) Mostrar Superhéroe más alto")
    print("6) Mostrar Superhéroe Masculino más alto")
    print("7) Mostrar Superhéroe Femenino más alto")
    print("8) Mostrar Superhéroe más bajo")
    print("9) Mostrar Superhéroe Masculino más bajo")
    print("10) Mostrar Superhéroe Femenino más bajo")
    print("11) Mostrar altura promedio")
    print("12) Mostrar altura promedio de los Superhérores masculinos")
    print("13) Mostrar altura promedio de los Superhérores femeninos")
    print("14) Mostrar Superhéroe más pesado y cuál es el menos pesado")
    print("15) Mostrar cantidad de Superhéroes por color de ojos")
    print("16) Mostrar cantidad de Superhéroes por color de pelo")
    print("17) Mostrar cantidad de Superhéroes por inteligencia")   
    print("18) Mostrar Superhéroes por color de ojos")
    print("19) Mostrar Superhéroes por color de pelo")
    print("20) Mostrar Superhéroes por inteligencia")
    print("0) Salir")
    opcion = input("Elija una opción » ")
    print(" ")
    return opcion

##########################################################################################################




def calcular_promedio_genero(lista:list,genero:str,valor:str,dato:str):
    """Calcula el promedio del valor que se desee del género elegido

    Args:
        lista (list): lista de donde se sacan los datos
        genero (str): clave para entrar al diccionario de generos
        valor (str): clave del valor que se quiere promediar
        dato (str): M para masculino, F para femenino

    Returns:
        float: Devuelve el promedio
    """
    listaHeroesGenero = listar_heroe_por_valor(lista,genero,dato)
    promedio = calcular_promedio(listaHeroesGenero,valor)
    return promedio


def calcular_menor_valor_genero(lista:list,genero:str,valor:str,dato:str)->float:
    """Calcula el menor valor pedido dependiendo del género

    Args:
        lista (list): Lista de dónde se sacan los datos
        genero (str): clave para entrar al diccionario de generos
        valor (str): segundo valor para calcular el peso o la altura mayor
        dato (str): M para masculino, F para femenino

    Returns:
        float: Devuelve un minimo
    """
    listaHeroesGenero = listar_heroe_por_valor(lista,genero,dato)
    minimoValor = buscar_minimo(listaHeroesGenero,valor)
    return minimoValor


def calcular_mayor_valor_genero(lista:list,genero:str,valor:str,dato:str)->float:
    """Calcula el maximo valor pedido dependiendo del género

    Args:
        lista (list): Lista de dónde se sacan los datos
        genero (str): clave para entrar al diccionario de generos
        valor (str): segundo valor para calcular el peso o la altura mayor
        dato (str): M para masculino, F para femenino

    Returns:
        float: Devuelve un máximo
    """
    listaHeroesGenero = listar_heroe_por_valor(lista,genero,dato)
    maximoValor = buscar_maximo(listaHeroesGenero,valor)
    return maximoValor


def mostrar_nombres_por_valor(lista:list,clave:str,dato:str):
    """Muestra los nombres según la clave asignada

    Args:
        lista (list): Lista de donde se buscan los nombres
        clave (str): Key para acceder al diccionario necesario
        dato (str): M para masculino, F para femenino
    """
    listaNombres = listar_heroe_por_valor(lista,clave,dato)
    mostrar_nombres(listaNombres)   


def listar_heroe_por_valor(lista:list,clave:str,dato:str):
    """Hace una lista con los nombres según el género que se pida

    Args:
        lista (list): Lista de dónde se sacan los nombres
        clave (str): Clave para acceder al género
        dato (str): M para buscar nombres masculinos y F para buscar nombres femeninos
    """
    listaHeroes = []
    for heroe in lista:
        genero = heroe[clave]
        nombreAux = heroe["nombre"]
        altura = heroe["altura"]
        peso = heroe["peso"]
        colorOjos = heroe["color_ojos"]
        colorPelo = heroe["color_pelo"]
        inteligencia = heroe["inteligencia"]

        if genero == dato:
            diccionarioHeroes = {}
            nombre = nombreAux
            diccionarioHeroes["nombre"] = nombre
            diccionarioHeroes[clave] = genero
            diccionarioHeroes["altura"] = altura
            diccionarioHeroes["peso"] = peso
            diccionarioHeroes["color_ojos"] = colorOjos
            diccionarioHeroes["color_pelo"] = colorPelo
            diccionarioHeroes["inteligencia"] = inteligencia
            listaHeroes.append(diccionarioHeroes)
            
    return listaHeroes

#***************************************************************************************************
def buscar_heroe_mayor_valor(lista:list,clave:str)->str:
    """Busca el nombre que tiene el mayor valor de la clave

    Args:
        lista (list): lista de donde se busca el nombre
        clave (str): valor que se pide 

    Returns:
        str: Nombre con mayor valor
    """
    mayorValue = buscar_maximo(lista,clave)
    for heroe in lista:
        target = float(heroe[clave])
        nombre = heroe["nombre"]
        if mayorValue == target:
            heroMayorValor = nombre
            return heroMayorValor

def buscar_heroe_menor_valor(lista:list,clave:str)->str:
    """Busca el nombre que tiene el menor valor de la clave

    Args:
        lista (list): lista de donde se busca el nombre
        clave (str): valor que se pide 

    Returns:
        str: Nombre con menor valor
    """
    menorValue = buscar_minimo(lista,clave)
    for heroe in lista:
        target = float(heroe[clave])
        nombre = heroe["nombre"]
        if menorValue == target:
            heroMenorValor = nombre
            return heroMenorValor
        
def concatenar_nombre_altura(lista:list):
    """Muestra la lista con el nombre y altura de los heroes

    Args:
        lista (list): Lista de donde se sacan los valores
    """
    for heroe in lista:
        nombre = heroe["nombre"]
        altura = float(heroe["altura"])
        print(f"» {nombre:>18}{altura:>20}")

def mostrar_altura(lista:list):
    """Recorre y muestra el listado de alturas de superheroes

    Args:
        lista (list): Lista a recorrer
    """
    for heroe in lista:
        alturaHeroe = float(heroe['altura'])
        mostrar(alturaHeroe)

def mostrar_nombres(lista:list):
    """Recorre y muestra el listado de nombres de superhéroes

    Args:
        lista (list): Lista a recorrer
    """
    for heroe in lista:
        nombreHeroe = heroe['nombre']
        mostrar(nombreHeroe)

def mostrar(variable:any)->str:
    """Muestra por consola un dato con decoración

    Arg:
        variable (any): Dato a ser mostrado
    """
    print(f"» {variable}")


######################################## CALCULOS ############################################

def contador(lista:list,clave:str,valor:str)->int:
    """Hace un contador según el valor que quieras contar

    Args:
        lista (list): lista de donde saca los datos
        clave (str): Clave para acceder al diccionario
        valor (str): valor que se quiere contar

    Returns:
        int: Devuelve la cantidad total
    """
    contador = 0
    for heroe in lista:
        color = heroe[clave]
        if color == valor:
            contador += 1
    return contador

def buscar_maximo(lista:list,clave:str)->float:
    """Busca el máximo en la lista

    Args:
        lista (list): lista a recorrer para buscar el máximo
        clave (str): clave de donde se quiere sacar el máximo

    Returns:
        float: devuelve el valor más grande
    """
    flag_maximo = True
    maximo = 0
    for heroe in lista:
        target = float(heroe[clave])
        
        if (maximo < target) or (flag_maximo == True):
            maximo = target
            flag_maximo = False
    
    return maximo

def buscar_minimo(lista:list,clave:str)->float:
    """Busca el mínimo en la lista

    Args:
        lista (list): lista a recorrer para buscar el mínimo
        clave (str): clave de donde se quiere sacar el mínimo
    Returns:
        float: devuelve el valor más chico
    """
    flag_minimo = True
    minimo = 0
    for heroe in lista:
        target = float(heroe[clave])
        
        if (minimo > target) or (flag_minimo == True):
            minimo = target
            flag_minimo = False
    
    return minimo

def calcular_promedio(lista:list,clave:str)->float:
    """Calcula el promedio

    Args:
        lista (list): lista de dónde se sacan los datos a calcular
        clave (str): valor que se quiere calcular

    Returns:
        float: Devuelve el resultado del promedio
    """
    contador = 0
    value = 0
    for target in lista:
        contador += 1
        value += float(target[clave])
    
    promedio = value / contador
    return promedio

########################################### VALIDACIONES ######################################

def validar_entero(validar,texto)->int:
    """Pide y valida el valor para que sea un entero

    Args:
        validar (any): Valor a validar
        texto (str): mensaje

    Returns:
        int: El valor ya validado
    """
    while True:
        validar = input(f"Ingrese el {texto} valor: \n")
        if (validar.isdigit()):
            validar = int(validar)
            break
        else:
            print("Eso no es un número positivo\n")

    return validar
