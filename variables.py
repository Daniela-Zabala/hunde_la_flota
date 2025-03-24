# Variables globales:

letras = ['A','B','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
estilo_tablero = {'punto':' · ', 'agua':' ~ ', 'barco':' O ','tocado':' X '}

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
        for n in range(2):
            print(end = ' ')
            [print(' ',n, end = ' ') for n in range(1,self.ndim + 1)]
            print(end = '   ')
        print()
        for fila1, fila2, letra in zip(self.flota, self.radar, self.letras):
            print(letra, end = ' ')
            for posicion1 in fila1:
                print(posicion1, end = ' ')
            print(' | ',letra, end = ' ')
            for posicion2 in fila2:
                print(posicion2, end = ' ')
            print()

    def check_barcos(self):
        if np.any(self.flota == estilo_tablero['barco']):
            return True
        else:
            return False
    
    def activar_radar(self, flota_enemigo):
        self.radar = np.where(flota_enemigo == estilo_tablero['barco'], estilo_tablero['punto'], flota_enemigo)
        return self.radar
