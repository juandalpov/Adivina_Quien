def mostrar_personajes(personajes):
    for p in personajes:
        print("- " + p['nombre'])

def buscar_personaje(personajes, nombre):
    for p in personajes:
        if p['nombre'].lower() == nombre.lower():
            return p
    return None