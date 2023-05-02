from data_stark import lista_personajes

def imprimirRespuesta(texto):
    print(texto)

def stark_normalizar_datos(lista:list):
    contadorDeModificaciones = 0
    if len(lista) == 0:
        mensaje = "Error, la lista esta vacia"
    else:
        for personaje in lista:
            if type(personaje["altura"]) == str:
                altura = float(personaje["altura"])
                personaje["altura"] = altura
                contadorDeModificaciones += 1
            elif type(personaje["peso"]) == str:
                peso = float(personaje["peso"])
                personaje["peso"] = peso
                contadorDeModificaciones += 1
            elif type(personaje["fuerza"]) == str:
                fuerza = int(personaje["fuerza"])
                personaje["fuerza"] = fuerza
                contadorDeModificaciones += 1
    
    if contadorDeModificaciones > 0:
        mensaje = "Datos normalizados"

def obtener_nombre(personaje:dict):
    nombre = personaje["nombre"]
    mensaje = "Nombre: " + nombre
    return mensaje

def stark_imprimir_nombres_heroes(listas:list):
    valor_lista = 0

    if len(listas) == 0:
        valor_lista = -1
        return valor_lista
    else:
        valor_lista = 1
        for personaje in listas:
            imprimirRespuesta(obtener_nombre(personaje))

def obtener_nombre_y_dato(personaje:dict, key:str):
    nombre = personaje
    dato = personaje[key]
    mensaje = f"Nombre: {nombre} | {key}: {dato}"

    return mensaje

def stark_imprimir_nombres_alturas(lista:list):
    valor_lista = 0

    if len(lista) == 0:
        valor_lista = -1
        return valor_lista
    else:
        valor_lista = 1
        for personaje in lista:
            imprimirRespuesta(obtener_nombre_y_dato(personaje["nombre"], "altura"))

def calcular_max(heroes:list, key:str):
    mayor_personaje = heroes[0]

    for heroe in heroes:
        if heroe[key] > mayor_personaje[key]:
            mayor_personaje = heroe
            nombreHeroeMayor = mayor_personaje["nombre"]
            keyHeroeMayor = mayor_personaje[key]
    mensaje = f"Personaje: {nombreHeroeMayor} | {key}: {keyHeroeMayor}"
    return mensaje

def calcular_min(heroes:list, key:str):
    menor_personaje = heroes[0]

    for heroe in heroes:
        if heroe[key] < menor_personaje[key]:
            menor_personaje = heroe
            nombreHeroeMenor = menor_personaje["nombre"]
            keyHeroeMenor = menor_personaje[key]
    mensaje = f"Personaje: {nombreHeroeMenor} | {key}: {keyHeroeMenor}"
    return mensaje

def calcular_max_min_dato(heroes:list, calculo:str, key:str):
    if calculo == "maximo":
        calcular_max(heroes, key)
    elif calculo == "minimo":
        calcular_min(heroes, key)

def stark_calcular_imprimir_heroe(heroes:list, calculo:str, key:str):
    valor_lista = 0
    if len(heroes) == 0:
        valor_lista == -1
        return valor_lista
    elif len(heroes) != 0:
        valor_lista == 1
        imprimirRespuesta(calcular_max_min_dato(heroes, calculo, key))

def sumar_dato_heroe(heroes:list, key:str):
    valor_lista = 0
    acumulador_heroes = 0
    if len(heroes) == 0:
        valor_lista = -1
        return valor_lista
    else:
        for heroe in heroes:
            acumulador_heroes = acumulador_heroes + heroe[key]
        return acumulador_heroes
    
def dividir(dividendo:int, divisor:int):
    if divisor == 0:
        return 0
    else:
        resultado = dividendo / divisor
        return resultado

def calcular_promedio(heroes:list, key:str):
    divisor = len(heroes)
    resultado = dividir(sumar_dato_heroe(heroes, "altura"), divisor)
    return resultado

def stark_calcular_imprimir_promedio_altura(heores:list, key:str):
    valor_lista = 0

    if len(heores) == 0:
        valor_lista = -1
        return valor_lista
    else:
        imprimirRespuesta(calcular_promedio(heores, key))

def imprimir_menu():
    menu = """\nCual opción va a elegir?
    \n1 - El nombre de todos los héroes
    \n2 - Altura de todos los heroes
    \n3 - Heroe mas alto
    \n4 - Heroe mas chico
    \n5 - Promedio Alturas
    \n0 - Salir del Programa
    """

    imprimirRespuesta(menu)