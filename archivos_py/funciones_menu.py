# Menú principal
def menu_principal():
    menu = '\n\t 1. Empezar a jugar\n\t 2. Juego rápido\n\t 3. Salir\n'
    eleccion = input(menu)

    while eleccion.isnumeric() != True or int(eleccion) > 4 or int(eleccion) <0:
        eleccion = input(menu)
    return int(eleccion)

# Función para mostrar instrucciones
def mostrar_instrucciones():
    print(""" 
    - Cada jugador tiene un tablero de 10x10.
    - Los barcos se colocan aleatoriamente en el tablero.
    - Los jugadores se turnan para disparar a una coordenada (fila, columna).
    - El impacto se marcará en el tablero:
        Impacto en barco -> X
        Impacto en Agua -> =
        Barco hundido -> O
    - El objetivo es hundir todos los barcos del rival.
    - En este caso el rival será CPU.
    - Cuando quieras abandonar la partida tan sólo escribe 'salir'.
    - ¡Buena suerte!
    """)

# Función para corregir mayúsculas y minúsculas del nombre
def corregir_nombre(nombre):
    return nombre.strip().lower().capitalize()  # Elimina espacios y convierte a minúsculas

# Presentación juego y pregunta por nombre
def inicio_juego():
    print(introduccion)

    #Coger el nombre del jugador
    nombre_jugador=input("\nPara empezar a jugar debes decir tu nombre\n")
    nombre_jugador = corregir_nombre(nombre_jugador) #Corregimos el nombre como hemos indicado arriba
    print("\nBienvenido",nombre_jugador) #Imrpimimos con la primera letra en mayuscula

    print(f"{nombre_jugador}, Estas son las reglas del juego:\n")
    mostrar_instrucciones()
    
    return nombre_jugador