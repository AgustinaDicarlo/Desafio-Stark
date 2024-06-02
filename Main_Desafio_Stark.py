from Funciones_Stark import *


seguir = True
listaDeHeroesF = listar_heroe_por_valor(lista_personajes,"genero","F")
listaDeHeroesM = listar_heroe_por_valor(lista_personajes,"genero","M")

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
            print("     || Superhéroe más alto ||")
            mayorTamaño = buscar_maximo(lista_personajes,"altura")
            heroeMayorTamaño = buscar_heroe_mayor_valor(lista_personajes,"altura")

            print(f"»{heroeMayorTamaño:>9}{mayorTamaño:>15}")
        case "6":
            print("|| Superhéroe Masculino más alto ||")

            mayorTamañoM = buscar_maximo(listaDeHeroesM,"altura")
            heroeMayorTamañoM = buscar_heroe_mayor_valor(listaDeHeroesM,"altura")

            print(f"»{heroeMayorTamañoM:>9}{mayorTamañoM:>15}")

        case "7":
            print("|| Superhéroe Femenino más alto ||")
            
            mayorTamañoF = buscar_maximo(listaDeHeroesF,"altura")
            heroeMayorTamañoF = buscar_heroe_mayor_valor(listaDeHeroesF,"altura")

            print(f"»{heroeMayorTamañoF:>9}{mayorTamañoF:>15}")

        case "8":
            print("     || Superhéroe más bajo ||")
            menorTamaño = buscar_minimo(lista_personajes,"altura")

            heroeMenorTamaño = buscar_heroe_menor_valor(lista_personajes,"altura")

            print(f"»{heroeMenorTamaño:>9}{menorTamaño:>15}")

        case "9":
            print("|| Superhéroe Masculino más bajo ||")
            menorTamañoM = buscar_minimo(listaDeHeroesM,"altura")
            heroeMenorTamañoM = buscar_heroe_menor_valor(listaDeHeroesM,"altura")

            print(f"»{heroeMenorTamañoM:>9}{menorTamañoM:>15}")
        case "10":
            print("|| Superhéroe Femenino más bajo ||")
            menorTamañoF = buscar_minimo(listaDeHeroesF,"altura")
            heroeMenorTamañoF = buscar_heroe_menor_valor(listaDeHeroesF,"altura")

            print(f"»{heroeMenorTamañoF:>9}{menorTamañoF:>15}")
        
        case "11":
            promedio = calcular_promedio(lista_personajes,"altura")
            print(f"La altura promedio es: {promedio:.2f}")

        case "12":
            promedioM = calcular_promedio_genero(lista_personajes,"genero","altura","M")
            print(f"La altura promedio en los héroes masculinos es: {promedioM:.2f}")
            
        case "13":
            promedioF = calcular_promedio_genero(lista_personajes,"genero","altura","F")
            print(f"La altura promedio en los héroes femeninos es: {promedioF:.2f}")

        case "14":
            print("| Superhéroe más y menos pesado |\n\n || Nombre ||     || Peso ||\n")
            mayorPeso = buscar_maximo(lista_personajes,"peso")
            menorPeso = buscar_minimo(lista_personajes,"peso")
            heroeMayorPeso = buscar_heroe_mayor_valor(lista_personajes,"peso")
            heroeMenorPeso = buscar_heroe_menor_valor(lista_personajes,"peso")
            
            print(f"»{heroeMayorPeso:>9}{mayorPeso:>15}\n» {heroeMenorPeso:>9}{menorPeso:>15}")
            
            
        case "0":
            respuesta = input("Desea salir? ").lower()
            if respuesta == "s":
                seguir = "n"
                continue
    pausar()

print("\n|| Programa Finalizado ||")