def recibir_disparo(tablero, coordenada):
    if tablero[coordenada] == estilo_tablero['barco']:
        tablero[coordenada] = estilo_tablero['tocado']
        print("Tocado")
        return True
    elif tablero[coordenada] == estilo_tablero['tocado']:
        print("Ya has disparado aquí")
        return False
    else:
        tablero[coordenada] = estilo_tablero['agua']
        print("Agua")
        return False

def disparo_coordenadas(tablero, coordenada):
    coord = coordenada.split(',')
    if len(coord) != 2:
        return False
    elif coord[0].upper() not in tablero.letras or int(coord[1]) > tablero.ndim:
        return False
    fila = letras.index(coord[0].upper())
    columna = int(coord[1])-1
    return (fila,columna)

def disparo_random(tablero):
    coordenada = (np.random.randint(0,len(tablero)-1),np.random.randint(0,len(tablero)-1))
    while tablero[coordenada] == 'X' or tablero[coordenada] == '~':
        coordenada = (np.random.randint(0,len(tablero)-1),np.random.randint(0,len(tablero)-1))
    recibir_disparo(tablero,coordenada)

def clear(): # Limpiar pantalla
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

def turno_batalla():
    duo = [jugador,cpu]

    while True:
        atacante, enemigo = duo[0], duo[1]

        print(f'Turno {atacante.name} - CAÑONAZOS: {atacante.disparos.count(True)}/{len(atacante.disparos)}')
        atacante.activar_radar(enemigo.flota)
        atacante.mostrar_tablero()

        if atacante.name == 'vision':
            print(f'Tablero {enemigo.name}')
            enemigo.activar_radar(atacante.flota)
            enemigo.mostrar_tablero()

        if atacante.tipo == 'jugador':
            coordenada = input('Introduce coordenada de disparo: ')
            if coordenada == 'salir':
                break
            disparo = disparo_coordenadas(enemigo, coordenada)
            while disparo == False:
                coordenada = input('Coordenadas incorrectas. Vuelve a intentarlo: ')
                disparo = disparo_coordenadas(enemigo, coordenada)
            acierto = recibir_disparo(enemigo.flota, disparo)
            atacante.disparos.append(acierto)
        else:
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
    
    print('Salida -> Función de menú')
    #quit()
