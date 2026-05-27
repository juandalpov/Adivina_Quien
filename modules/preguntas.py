def mostrar_preguntas():
    print("1. ¿Tiene gafas?")
    print("2. ¿Tiene sombrero?")
    print("3. ¿Tiene barba?")
    print("4. ¿Tiene el cabello negro?")
    print("5. ¿Es mujer?")
    print("6. Intentar adivinar el personaje")

def responder_pregunta(opcion, personaje_secreto):
    if opcion == "1":
        if personaje_secreto['gafas'] == "si":
            return "sí"
        return "no"
    elif opcion == "2":
        if personaje_secreto['sombrero'] == "si":
            return "sí"
        return "no"
    elif opcion == "3":
        if personaje_secreto['barba'] == "si":
            return "sí"
        return "no"
    elif opcion == "4":
        if personaje_secreto['cabello'] == "negro":
            return "sí"
        return "no"
    elif opcion == "5":
        if personaje_secreto['genero'] == "femenino":
            return "sí"
        return "no"
    return ""