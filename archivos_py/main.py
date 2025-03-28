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