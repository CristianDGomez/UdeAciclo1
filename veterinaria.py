def veterinaria(nombres, tipos, edades, pesos):
    # ACÁ INICIA LA FUNCIÓN VETERINARIA

    diccionario = {}
    for i in range(len(nombres)):
        lista = [nombres[i], tipos[i], edades[i], pesos[i]]
        diccionario[str(i + 1)] = lista

    beneficiarios_can_fel = {}
    edadesparasuma2 = []
    k = 0
    for i in range(len(nombres)):
        if edades[i] >= 9 and (tipos[i] == 'canino' or tipos[i] == 'felino'):
            k += 1
            edadesparasuma2.append(edades[i])
            lista = [nombres[i], tipos[i], pesos[i]]
            beneficiarios_can_fel[str(k)] = lista

    while True:
        try:
            promedio_can_fel = sum(edadesparasuma2) / len(edadesparasuma2)
            break
        except ZeroDivisionError:
            promedio_can_fel = None
            break
    beneficiarios_equ_bov = {}
    k = 0
    edadesparasuma3 = []
    for i in range(len(nombres)):
        if edades[i] >= 16 and (tipos[i] == 'equino' or tipos[i] == 'bovino'):
            k += 1
            edadesparasuma3.append(edades[i])
            lista = [nombres[i], tipos[i], pesos[i]]
            beneficiarios_equ_bov[str(k)] = lista

    while True:
        try:
            promedio_equ_bov = sum(edadesparasuma3) / len(edadesparasuma3)
            break
        except ZeroDivisionError:
            promedio_equ_bov = None
            break
    return diccionario, beneficiarios_can_fel, beneficiarios_equ_bov, promedio_can_fel, promedio_equ_bov
