# Titulo del juego:

introduccion= "\nBienvenid@ a Hundir la Flota Team 5\n"

# Tablero:

letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
estilo_tablero = {'punto':' · ', 'agua':' = ', 'barco':' O ','tocado':' X '}
barcos= [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

# Jugadores:

class Jugador:
    def __init__(self, name, ndim = 10, tipo = 'jugador'):
        self.name = name
        self.tipo = tipo
        self.disparos = []

        tablero = np.full((2,ndim,ndim),estilo_tablero['punto'])
        self.flota, self.radar = tablero[0], tablero[1]
        self.ndim = ndim
        self.letras = letras[:ndim]

    def mostrar_tablero(self):
        ndim = len(self.flota)
        print()
        for fila in range(ndim):
            if fila == 0:
                print(end = '  ')
                for n in range(2):
                    [print(' ', n, end = ' ') for n in range(1,self.ndim + 1)]
                    print('\t', end = '  ')
            print('\n',letras[fila], end = ' ')
            [print(posicion, end = ' ') for posicion in self.flota[fila]]
            print('\t', letras[fila], end = ' ')
            [print(posicion, end = ' ') for posicion in self.radar[fila]]
        print()

    def check_barcos(self):
        if np.any(self.flota == estilo_tablero['barco']):
            return True
        else:
            return False
    
    def activar_radar(self, flota_enemigo):
        self.radar = np.where(flota_enemigo == estilo_tablero['barco'], estilo_tablero['punto'], flota_enemigo)
        return self.radar

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

# Limpiar pantalla

def clear(): # Limpiar pantalla
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

# Funciones colocar flota

def colocar_barco(tamaño, jugador):
    if jugador.tipo == 'jugador':
        salida = _colocar_barco_jugador(tamaño, jugador)
        if salida == 'salida':
            return salida
    else: 
        _colocar_barco_cpu(tamaño, jugador.flota)
        
def _colocar_barco_jugador(tamaño, jugador):
    """Función dedicada a colocar barcos para el jugador humano"""
    print(f"Colocando barco de tamaño {tamaño}")
    while True:
        try:
            fila, columna = _obtener_coordenadas_jugador(tamaño, jugador.flota)
            if fila == 'salida':
                return 'salida'  # Solo devuelve 'salida' si el usuario quiere salir
                
            direccion = _obtener_direccion_jugador()
            
            if not _posicion_valida(fila, columna, direccion, tamaño, jugador.flota):
                print("Posición no válida (fuera del tablero o superposición). Intenta de nuevo.")
                continue

            _colocar_barco_en_tablero(fila, columna, direccion, tamaño, jugador.flota)
            break  # Sale del bucle cuando el barco se coloca correctamente

        except (ValueError, IndexError):
            print("Coordenada no válida. Intenta de nuevo.")
    
    return None  # No devuelve 'salida' a menos que el usuario quiera salir

def _obtener_coordenadas_jugador(tamaño, tablero):
        """Obtiene y valida las coordenadas del jugador"""
        inicio = input(f"Barco de tamaño {tamaño}. Ingresa la coordenada de inicio (ej. A1): ").upper()
        
        if inicio == 'salir' or inicio == "SALIR" or inicio == "Salir":
            return 'salida','salida'

        fila = ord(inicio[0]) - ord('A')
        columna = int(inicio[1:]) - 1
        
        if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero):
            print("Coordenada fuera del tablero. Intenta de nuevo.")
            raise ValueError("Coordenada fuera de rango")
            
        return fila, columna

def _obtener_direccion_jugador():
        """Obtiene y valida la dirección del barco"""
        direccion = input("Ingresa la dirección (H para horizontal, V para vertical): ").upper()
        if direccion not in ['H', 'V']:
            print("Dirección no válida. Intenta de nuevo.")
            raise ValueError("Dirección no válida")
        return direccion

def _posicion_valida(fila, columna, direccion, tamaño, tablero):
    """Verifica si la posición es válida (sin salirse del tablero ni superponerse)."""
    if direccion == 'H':
        if columna + tamaño > len(tablero[0]):
            return False
        return all(tablero[fila][columna + i] == estilo_tablero['punto'] for i in range(tamaño))
    else:
        if fila + tamaño > len(tablero):
            return False
        return all(tablero[fila + i][columna] == estilo_tablero['punto'] for i in range(tamaño))

def _colocar_barco_en_tablero(fila, columna, direccion, tamaño, tablero):
    """Coloca físicamente el barco en el tablero"""
    if direccion == 'H':
        # Coloca horizontalmente (mismo fila, columnas consecutivas)
        for i in range(tamaño):
            if columna + i < len(tablero[0]):  # Verifica límites del tablero
                tablero[fila][columna + i] = estilo_tablero['barco']
    else:
        # Coloca verticalmente (misma columna, filas consecutivas)
        for i in range(tamaño):
            if fila + i < len(tablero):  # Verifica límites del tablero
                tablero[fila + i][columna] = estilo_tablero['barco']

def _colocar_barco_cpu(tamaño, tablero):
    """Función dedicada a colocar barcos para la CPU"""
    while True:
        fila = random.randint(0, len(tablero) - 1)
        columna = random.randint(0, len(tablero) - 1)
        direccion = random.choice(['H', 'V'])

        if _posicion_valida(fila, columna, direccion, tamaño, tablero): 
            _colocar_barco_en_tablero(fila, columna, direccion, tamaño, tablero) 
            break
# Funciones de disparo

def recibir_disparo(tablero, coordenada):
    if tablero[coordenada] == estilo_tablero['barco']:
        tablero[coordenada] = estilo_tablero['tocado']
        input("¡¡TOCADO!!.\n(Presiona 'Enter' para continuar")
        return True
    elif tablero[coordenada] == estilo_tablero['tocado']:
        input("Almirante, ¿está usted ebrio? Ya ha disparado aquí.\n(Presiona 'Enter' para continuar")
        return False
    else:
        tablero[coordenada] = estilo_tablero['agua']
        input("Agua.\n(Presiona 'Enter' para continuar")
        return False

def disparo_coordenadas(tablero, coordenada):    
    fila, columna = coordenada[0], coordenada[1:]
    if len(coordenada) > 3:
        return False
    elif columna.isnumeric() != True:
        return False
    elif fila.upper() not in tablero.letras or int(columna) > tablero.ndim:
        return False
    fila = letras.index(fila.upper())
    columna = int(columna)-1
    return (fila,columna)

def disparo_random(tablero):
    coordenada = (np.random.randint(0,len(tablero)-1),np.random.randint(0,len(tablero)-1))
    while tablero[coordenada] == estilo_tablero["tocado"] or tablero[coordenada] == estilo_tablero["agua"]:
        coordenada = (np.random.randint(0,len(tablero)-1),np.random.randint(0,len(tablero)-1))
    recibir_disparo(tablero,coordenada)

# Función de juego 

def turno_batalla(jugador, cpu):
    duo = [jugador,cpu]

    while True:
        atacante, enemigo = duo[0], duo[1]

        if atacante.name == 'vision' or atacante.name == 'Vision':
            print(f'Tablero {cpu.name}')
            enemigo.activar_radar(jugador.flota)
            enemigo.mostrar_tablero()

        if atacante.tipo == 'jugador':
            print(f'Turno {atacante.name} \t\t CAÑONAZOS: {atacante.disparos.count(True)}/{len(atacante.disparos)}')
            jugador.activar_radar(cpu.flota)
            jugador.mostrar_tablero()
            
            coordenada = input('Introduce coordenada de disparo: ')
            disparo = disparo_coordenadas(enemigo, coordenada)
            if coordenada == 'salir' or coordenada == "SALIR" or coordenada == "Salir":
                break
            while disparo == False:
                coordenada = input('Coordenadas incorrectas. Vuelve a intentarlo: ')
                disparo = disparo_coordenadas(enemigo, coordenada)
            acierto = recibir_disparo(enemigo.flota, disparo)
            atacante.disparos.append(acierto)
        else:
            print(f'Turno {atacante.name} \t\t CAÑONAZOS: {atacante.disparos.count(True)}/{len(atacante.disparos)}')
            acierto = disparo_random(enemigo.flota) 
            atacante.disparos.append(acierto)
        
        if acierto == True:
            if enemigo.check_barcos() != True:
                print('Ganaste')
                break
        else:
            duo.reverse()
            continue
    
        clear
        ()    # Limpiamos la pantalla (no funciona en notebooks)
    
    return 'salida'

## MAIN ##

import numpy as np
import os
import random

while True:
    print(introduccion)
    eleccion = menu_principal()

    if eleccion == 1:
        nombre_jugador = inicio_juego()
        usuario = Jugador(nombre_jugador)
        cpu = Jugador('CPU',tipo='cpu')
        for i in [cpu, usuario]:
            for tamaño in barcos:
                colocar_flota = colocar_barco(tamaño= tamaño, jugador=i)
                if i.tipo == 'jugador':
                    if colocar_flota == 'salida':
                        break
                    print(f"\nTablero {i.name}:")
                    i.mostrar_tablero()
        if colocar_flota == 'salida':
            continue
    elif eleccion == 2:
        nombre_jugador = inicio_juego()
        usuario = Jugador(nombre_jugador)
        cpu = Jugador('CPU',tipo='cpu')
        for i in [cpu, usuario]:
            for tamaño in barcos:
                _colocar_barco_cpu(tamaño = tamaño, tablero = i.flota)
    elif eleccion == 3:
        break

    input(f"Almirante {usuario.name} su flota está lista.\n(Presiona 'Enter' para continuar)")
    batalla = turno_batalla(usuario, cpu)
    if batalla == 'salida':
        continue

quit()