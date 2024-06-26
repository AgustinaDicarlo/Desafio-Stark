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
        
        case "15":
            print("         || Cantidad de Héroes según el color de ojos ||")
            colorMarron = contador(lista_personajes,"color_ojos","Brown")
            colorAzul = contador(lista_personajes,"color_ojos","Blue")
            colorAmarillo = contador(lista_personajes,"color_ojos","Yellow (without irises)")
            colorYellow = contador(lista_personajes,"color_ojos","Yellow")
            colorTotalAmarillo = colorAmarillo + colorYellow
            colorHazel = contador(lista_personajes,"color_ojos","Hazel")
            colorPlateado = contador(lista_personajes,"color_ojos","Silver")
            colorRojo = contador(lista_personajes,"color_ojos","Red")

            print(f"Ojos Marrones: {colorMarron}\nOjos Azules: {colorAzul}\nOjos Amarillos: {colorTotalAmarillo}\nOjos Hazel: {colorHazel}\nOjos Plateados: {colorPlateado}\nOjos Rojos: {colorRojo}")
        
        case "16":
            print("     || Cantidad de Héroes según el color de pelo ||")

            colorAmarilloP = contador(lista_personajes,"color_pelo","Yellow")
            colorMarronP = contador(lista_personajes,"color_pelo","Brown")
            colorNegro = contador(lista_personajes,"color_pelo","Black")
            colorAuburn = contador(lista_personajes,"color_pelo","Auburn")
            colorRO = contador(lista_personajes,"color_pelo","Red / Orange")
            colorBlanco = contador(lista_personajes,"color_pelo","White")
            colorN = contador(lista_personajes,"color_pelo","No Hair")
            colorNE = contador(lista_personajes,"color_pelo","")
            colorNN = colorN + colorNE
            colorRubio = contador(lista_personajes,"color_pelo","Blond")
            colorVerde = contador(lista_personajes,"color_pelo","Green")
            colorMB = contador(lista_personajes,"color_pelo","Brown / White")

            print(f"Pelo Amarillo: {colorAmarilloP}\nPelo Marrón: {colorMarronP}\nPelo Negro: {colorNegro}\nPelo Auburn: {colorAuburn}\nPelo Rojo/Naranja: {colorRO}\nPelo Blanco: {colorBlanco}\nNo tiene: {colorNN}\nPelo Rubio: {colorRubio}\nPelo Verde: {colorVerde}\nPelo Marrón / Blanco: {colorMB}")

        case "17":
            print(" || Cantidad de Héroes según su inteligencia || ")

            inteligenciaBuena = contador(lista_personajes,"inteligencia","good")
            inteligenciaPromedio = contador(lista_personajes,"inteligencia","average")
            inteligenciaAlta = contador(lista_personajes,"inteligencia","high")
            inteligenciaCero = contador(lista_personajes,"inteligencia","")

            print(f"Alta: {inteligenciaAlta}\nBuena: {inteligenciaBuena}\nPromedio: {inteligenciaPromedio}\nNo tiene: {inteligenciaCero}\n")
        
        case "18":
            print("|| Superhéroes por color de Ojos ||\n")
            print("\n« Ojos Marrones »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_ojos","Brown")
            pausar()
            print("\n« Ojos Azules »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_ojos","Blue")
            pausar()
            print("\n« Ojos Amarillos »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_ojos","Yellow (without irises)")
            mostrar_nombres_por_valor(lista_personajes,"color_ojos","Yellow")
            pausar()
            print("\n« Ojos Hazel »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_ojos","Hazel")
            pausar()
            print("\n« Ojos Plateados »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_ojos","Silver")
            pausar()
            print("\n« Ojos Rojos »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_ojos","Red")

            print("\n                   || Listado Terminado ||")

        case "19":
            print("|| Superhéroes por color de Pelo ||\n")
            print("\n« Pelo Amarillo »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","Yellow")
            pausar()
            print("\n« Pelo Marrón »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","Brown")
            pausar()
            print("\n« Pelo Negro »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","Black")
            pausar()
            print("\n« Pelo Auburn »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","Auburn")
            pausar()
            print("\n« Pelo Rojo / Naranja »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","Red / Orange")
            pausar()
            print("\n« Pelo Blanco »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","White")
            pausar()
            print("\n« No tiene »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","No Hair")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","")
            pausar()
            print("\n« Pelo Rubio »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","Blond")
            pausar()
            print("\n« Pelo Verde »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","Green")
            pausar()
            print("\n« Pelo Marrón / Blanco »\n")
            mostrar_nombres_por_valor(lista_personajes,"color_pelo","Brown / White")

            print("\n                   || Listado Terminado ||")
        case "20":
            print("|| Superhéroes por Inteligencia ||\n")
            print("\n«Nivel de Inteligencia: Alta »\n")
            mostrar_nombres_por_valor(lista_personajes,"inteligencia","high")
            pausar()
            print("\n«Nivel de Inteligencia: Buena »\n")
            mostrar_nombres_por_valor(lista_personajes,"inteligencia","good")
            pausar()
            print("\n«Nivel de Inteligencia: Promedio »\n")
            mostrar_nombres_por_valor(lista_personajes,"inteligencia","average")
            pausar()
            print("\n«Nivel de Inteligencia: No tiene »\n")
            mostrar_nombres_por_valor(lista_personajes,"inteligencia","")

            print("\n                   || Listado Terminado ||")
        case "0":
            respuesta = input("Desea salir? ").lower()
            if respuesta == "s":
                seguir = "n"
                continue
    pausar()

print("\n|| Programa Finalizado ||")