def leer_personajes(ruta_archivo):
    personajes = []
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        encabezados = lineas[0].strip().split(',')
        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            personaje = {}
            for i in range(len(encabezados)):
                personaje[encabezados[i]] = valores[i]
            personajes.append(personaje)
    return personajes