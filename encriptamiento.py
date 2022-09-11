from string import ascii_uppercase as alfabeto

def encriptador(mensaje):
    unicos = list(mensaje)
    unicos = set(unicos)
    clave = dict(zip(unicos, alfabeto))
    minidic = {}
    for letra in unicos:
        minidic[letra] = clave[letra]
    encriptado = ""
    for i in mensaje:
        encriptado = encriptado + clave[i]
    return encriptado, clave

def desencriptador(encriptado, clave):
    listakeys = list(clave.keys())
    listavalores = list(clave.values())
    desencriptado = ''
    for valor in encriptado:
        indice = listavalores.index(valor)
        desencriptado = desencriptado + listakeys[indice]
    return desencriptado