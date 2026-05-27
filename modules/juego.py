import random
import time
from modules.cargar_datos import leer_personajes
from modules.personajes import mostrar_personajes
from modules.preguntas import mostrar_preguntas, responder_pregunta
from modules.archivos import guardar_historial

def iniciar_juego():
    personajes = leer_personajes('data/personajes.txt')
    personaje_secreto = random.choice(personajes)
    
    print("¡Bienvenido a Adivina Quién!")
    nombre_jugador = input("Ingresa tu nombre: ")
    
    print("\nPersonajes disponibles:")
    mostrar_personajes(personajes)
    
    preguntas_usadas = 0
    jugando = True
    
    while jugando:
        print("\nMenú de preguntas:")
        mostrar_preguntas()
        opcion = input("Elige una opción (1-6): ")
        
        if opcion in ["1", "2", "3", "4", "5"]:
            respuesta = responder_pregunta(opcion, personaje_secreto)
            print(f"Respuesta: {respuesta.upper()}")
            preguntas_usadas += 1
            
            # El programa hace una pausa de 2 segundos para que alcances a leer
            time.sleep(2)
            
        elif opcion == "6":
            intento = input("Escribe el nombre del personaje: ")
            preguntas_usadas += 1
            if intento.lower() == personaje_secreto['nombre'].lower():
                print("¡Felicidades! Adivinaste el personaje secreto.")
                guardar_historial(nombre_jugador, "ganó", personaje_secreto['nombre'], preguntas_usadas)
            else:
                print(f"Perdiste. El personaje secreto era {personaje_secreto['nombre']}.")
                guardar_historial(nombre_jugador, "perdió", personaje_secreto['nombre'], preguntas_usadas)
            jugando = False
        else:
            print("Opción no válida.")
            time.sleep(1.5)
    
    print("Fin del juego.")