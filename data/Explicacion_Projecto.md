# Explicación del Proyecto

El proyecto se dividió en módulos dentro de la carpeta `modules` para separar responsabilidades. `cargar_datos.py` lee el archivo `.txt` dinámicamente usando los encabezados y convierte la información en una lista de diccionarios. `juego.py` controla el ciclo principal, el contador de turnos y selecciona el personaje al azar usando `random`. `preguntas.py` expone el menú de opciones y evalúa las características del personaje. `personajes.py` maneja la iteración para mostrar la información en pantalla. `archivos.py` registra los resultados anexando líneas nuevas a `historial.txt`.

Se utilizaron listas para agrupar a todos los personajes y diccionarios para representar las llaves y valores individuales (ej: `"nombre": "Ana"`). Los archivos `.txt` permitieron la persistencia de datos. El principal reto fue coordinar correctamente los imports entre módulos y asegurar que el flujo del menú no se rompiera ante respuestas inesperadas.
