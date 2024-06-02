from Funciones_Stark import *


seguir = True
while seguir == True:
    
    match menu():
        case "1":
            print("        || Nombre de Superhéroes ||")
            mostrar_nombres(lista_personajes)
            
        case "2":
            print("        || Superhéroes Masculinos ||")
            mostrar_nombres_por_valor(lista_personajes,"genero","M")

        case "3":
            print("        || Superhéroes Femeninos ||")
            mostrar_nombres_por_valor(lista_personajes,"genero","F")

        case "4":
            print("   || Superhéroes ||           || Alturas ||\n")
            concatenar_nombre_altura(lista_personajes)
            
        case "5":
            print("|| Superhéroe más alto ||")
            print(buscar_heroe_mayor_valor(lista_personajes,"altura"))
            
        case "6":
            print("|| Superhéroe más bajo ||")
            print(buscar_heroe_menor_valor(lista_personajes,"altura"))
            
        case "7":
            promedio = calcular_promedio(lista_personajes,"altura")
            print(f"La altura promedio es: {promedio:.2f}")
            
        case "8":
            print("| Superhéroe más y menos pesado |\n\n || Nombre ||     || Peso ||\n")
            mayorPeso = buscar_maximo(lista_personajes,"peso")
            menorPeso = buscar_minimo(lista_personajes,"peso")
            heroeMayorPeso = buscar_heroe_mayor_valor(lista_personajes,"peso")
            heroeMenorPeso = buscar_heroe_menor_valor(lista_personajes,"peso")
            
            print(f"»{heroeMayorPeso:>9}{mayorPeso:>15}\n»{heroeMenorPeso:>9}{menorPeso:>15}")
            
            
        case "9":
            respuesta = input("Desea salir? ").lower()
            if respuesta == "s":
                seguir = "n"
                continue
    pausar()

print("\n|| Programa Finalizado ||")