def guardar_historial(nombre_jugador, resultado, personaje, preguntas_usadas):
    with open('data/historial.txt', 'a', encoding='utf-8') as archivo:
        linea = f"Jugador: {nombre_jugador} | Resultado: {resultado} | Personaje: {personaje} | Preguntas usadas: {preguntas_usadas}\n"
        archivo.write(linea)