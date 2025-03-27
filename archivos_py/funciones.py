def clear(): # Limpiar pantalla
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

## FUNCIONES DE DISPARO ##

def recibir_disparo(tablero, coordenada):
    if tablero[coordenada] == estilo_tablero['barco']:
        tablero[coordenada] = estilo_tablero['tocado']
        return True
    elif tablero[coordenada] == estilo_tablero['tocado']:
        print("Ya has disparado aquí")
        return False
    else:
        tablero[coordenada] = estilo_tablero['agua']
        print("Agua")
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
    while tablero[coordenada] == 'X' or tablero[coordenada] == '~':
        coordenada = (np.random.randint(0,len(tablero)-1),np.random.randint(0,len(tablero)-1))
    recibir_disparo(tablero,coordenada)

## FUNCION DE JUEGO ##

def turno_batalla():
    duo = [jugador,cpu]

    while True:
        atacante, enemigo = duo[0], duo[1]

        if atacante.name == 'vision':
            print(f'Tablero {cpu.name}')
            enemigo.activar_radar(jugador.flota)
            enemigo.mostrar_tablero()

        if atacante.tipo == 'jugador':
            print(f'Turno {atacante.name} \t\t CAÑONAZOS: {atacante.disparos.count(True)}/{len(atacante.disparos)}')
            jugador.activar_radar(cpu.flota)
            jugador.mostrar_tablero()
            
            coordenada = input('Introduce coordenada de disparo: ')
            disparo = disparo_coordenadas(enemigo, coordenada)
            if coordenada == 'salir':
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
    
        clear()    # Limpiamos la pantalla (no funciona en notebooks)
    
    return 'salida'