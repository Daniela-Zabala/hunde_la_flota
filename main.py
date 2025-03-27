import numpy
import os

from .variables import *
from .funciones import *
from .instrucciones import *

jugador = Jugador('Victor')
cpu = Jugador('cpu', tipo = 'cpu')

barcos = [(1,4),(2,4),(3,4),(5,6),(5,7),(5,8)]
disparos = [(1,4), (0,4), (5,4), (5,5), (5,6), (5,7)]
for disparo,barco in zip(disparos,barcos):
    jugador.flota[barco] = estilo_tablero['barco']
    cpu.flota[disparo] = estilo_tablero['barco']

mostrar_instrucciones()
turno_batalla()

