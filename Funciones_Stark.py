from data_stark import *
import os





""" A. Analizar detenidamente el set de datos

C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
la altura del mismo
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F. Recorrer la lista y determinar la altura promedio de los superhéroes
(PROMEDIO)
G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
I. Ordenar el código implementando una función para cada uno de los valores
informados.
J. Construir un menú que permita elegir qué dato obtener """


def limpiar_pantalla():
    os.system("cls")

def pausar():
    os.system("pause")


def menu():
    limpiar_pantalla()
    print("             Stark Industries")
    print("--------------------------------------------")
    print("1) Mostrar el nombre de los Superhéroes")
    print("2) Mostrar Superhéroes con su altura")
    print("3) Mostrar Superhéroe más alto")
    print("4) Mostrar Superhéroe más bajo")
    print("5) Mostrar altura promedio")
    print("6) Mostrar Superhéroe más pesado y cuál es el menos pesado")
    print("7) Salir")
    opcion = input("Elija una opción » ")
    return opcion




def mostrar_nombre(lista:list):
    for heroe in lista:
        nombreHeroe = heroe['nombre']
        print(f"Nombre: {nombreHeroe}")


def mostrar_peso(lista:list):
    for heroe in lista:
        alturaHeroe = float(heroe['altura'])
        print(f"Altura: {alturaHeroe}")
