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
    return mayor_personaje[key]

def calcular_max(heroes:list, key:str):
    menor_personaje = heroes[0]

    for heroe in heroes:
        if heroe[key] > menor_personaje[key]:
            menor_personaje = heroe
    return menor_personaje[key]

def stark_calcular_imprimir_heroe(heroes:list, calculo:str, key:str):
    lista_vacia = 0
    if len(heroes) == 0:
        lista_vacia == -1
    elif 
