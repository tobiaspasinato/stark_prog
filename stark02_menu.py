from stark02_functions import*
from os import system

while True:
    print("""\nCual opción va a elegir?
    \n1 - El nombre de todos los héroes
    \n2 - Altura de todos los heroes
    \n0 - Salir del Programa
    """)
    
    opcion = int(input("Cual opción va a elegir? "))

    if opcion == 0:
        break
    elif opcion == 1:
        stark_imprimir_nombres_heroes(lista_personajes)
    elif opcion == 2:
        stark_imprimir_nombres_alturas(lista_personajes)
    elif opcion == 3:
        stark_calcular_imprimir_heroe(lista_personajes, "maximo", "altura")
system("cls")
print("Fin del Programa")
