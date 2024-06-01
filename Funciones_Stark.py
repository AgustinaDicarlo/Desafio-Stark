from data_stark import *
import os


################################################## MENÚ #####################################################

def limpiar_pantalla():
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
    print("2) Mostrar nombre y altura de los Superhéroes")
    print("3) Mostrar Superhéroe más alto")
    print("4) Mostrar Superhéroe más bajo")
    print("5) Mostrar altura promedio")
    print("6) Mostrar Superhéroe más pesado y cuál es el menos pesado")
    print("7) Salir")
    opcion = input("Elija una opción » ")
    print(" ")
    return opcion

#############################################################################################################



def buscar_heroe_mayor_valor(lista:list,clave:str):
    mayorValue = buscar_maximo(lista,clave)
    for heroe in lista:
        target = float(heroe[clave])
        nombre = heroe["nombre"]
        if mayorValue == target:
            heroMayorValor = nombre
            return heroMayorValor

def buscar_heroe_menor_valor(lista:list,clave:str):
    menorValue = buscar_minimo(lista,clave)
    for heroe in lista:
        target = float(heroe[clave])
        nombre = heroe["nombre"]
        if menorValue == target:
            heroMenorValor = nombre
            return heroMenorValor
        

def concatenar_nombre_altura(lista:list):
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


def mostrar(variable):
    """Muestra por consola un dato con decoración

    Arg:
        variable (any): Dato a ser mostrado
    """
    print(f"» {variable}")

######################################## CALCULOS ############################################

def buscar_maximo(lista:list,clave):
    """Busca el máximo en la lista

    Args:
        lista (list): lista a recorrer para buscar el máximo

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

def buscar_minimo(lista:list,clave):
    """Busca el mínimo en la lista

    Args:
        lista (list): lista a recorrer para buscar el mínimo

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

def calcular_promedio(lista:list,clave):
    contador = 0
    value = 0
    for target in lista:
        contador += 1
        value += float(target[clave])
    
    promedio = value / contador
    return promedio

##############################################################################################


########################################### VALIDACIONES ######################################

def validar_entero(validar,texto):
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

##############################################################################################