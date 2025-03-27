# Titulo del juego:

introduccion= "\nBiennvenid@ a Hundir la Flota Team 5"

# Tablero:

letras = ['A','B','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
estilo_tablero = {'punto':' · ', 'agua':' = ', 'barco':' O ','tocado':' X '}

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
