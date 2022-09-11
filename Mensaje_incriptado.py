from string import ascii_uppercase as alfabeto


def encriptador(mensaje):
    alfabeto = list(mensaje)
    clave = []
    encriptado = []

    for encriptado in clave:
        encriptado.append(alfabeto[encriptado])

    return encriptado, clave


def desencriptador(encriptado, clave):

    for encriptado in range(len(encriptado)):
        iniciador = clave.index()
        encriptado.append(encriptado[iniciador])
    desencriptado = "".join(encriptado)
    return desencriptado


print(desencriptador, encriptador)
