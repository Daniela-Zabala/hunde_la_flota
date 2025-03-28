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