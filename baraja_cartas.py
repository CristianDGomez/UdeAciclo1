def tiene_cartas_altas(cartas_siguientes):
    for i in cartas_siguientes:
        if i 'KQJA':
            return True
    return not(True)

def juego(baraja):
    n = len(baraja)
    j_actual = 'jugador1'
    p_j1 = 0
    p_j2 = 0
    for J,K in enumerate(baraja):
        puntos = 0
        n_crestan = n-1-j
        if K == 'A' and n_crestan >= 1 and not(tiene_cartas_altas(baraja[j+1])):
            puntos=1
        elif K == 'J' and  n_crestan >= 2 and not(tiene_cartas_altas(baraja[j+1:j+3])):
            puntos = 2
        elif K == 'Q' and n_crestan >= 3 and not(tiene_cartas_altas(baraja[j+1:j+5])):
            puntos = 3
        elif K == 'K' and n_crestan >= 4 and not(tiene_cartas_altas(baraja[j+1:j+5])):
            puntos = 4
        if j_actual == 'jugador1':
            p_j1 = puntos + p_j1
            j_actual = 'jugador2'
        else:
            p_j2 = puntos + p_j2
            j_actual = 'jugador1'

    return p_j1,p_j2