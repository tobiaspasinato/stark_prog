from stark02_functions import*
from os import system

stark_normalizar_datos(lista_personajes)

while True:
    imprimir_menu()
    
    opcion = int(input("Cual opción va a elegir? "))

    if opcion == 0:
        break
    elif opcion == 1:
        stark_imprimir_nombres_heroes(lista_personajes)
    elif opcion == 2:
        stark_imprimir_nombres_alturas(lista_personajes)
    elif opcion == 3:
        stark_calcular_imprimir_heroe(lista_personajes, "maximo", "altura")
    elif opcion == 4:
        stark_calcular_imprimir_heroe(lista_personajes, "minimo", "altura")
    elif opcion == 5:
        stark_calcular_imprimir_promedio_altura(lista_personajes, "altura")
    elif opcion == 6:
        stark_calcular_imprimir_heroe(lista_personajes, "maximo", "peso")
    elif opcion == 7:
        stark_calcular_imprimir_heroe(lista_personajes, "minimo", "peso")

system("cls")
print("Fin del Programa")
