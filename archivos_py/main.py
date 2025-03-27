import numpy as np
from .variables import *
from .menu import *
from .funciones import *

while True:
    eleccion = menu_principal()

    if eleccion == 1:
        nombre_jugador = inicio_juego()

        jugador = Jugador(nombre_jugador)
        cpu = Jugador('CPU','cpu')

        #colocar = colocar_barcos()
        batalla = turno_batalla()
        if batalla == 'salida':
            continue
    elif eleccion == 2:
        print('creditos')
    elif eleccion == 3:
        break

print('quit()')