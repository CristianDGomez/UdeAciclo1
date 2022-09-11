import numpy as np
import random

def encriptado(texto):
    medidaTexto = len(texto)
    n = (medidaTexto) ** (1 / 2)
    if (n // 1) != n:
        n = (n // 1) + 1
    n = int(n)
    for i in range(len(texto), n ** 2):
        texto = texto + "_"
    texto = list(texto)

    clave = []
    for i in range(len(texto)):
        clave.append(i)
    random.shuffle(clave)
    desordenado = []
    for i in clave:
        desordenado.append(ord(texto[i]))
    array_encriptado = np.array(desordenado).reshape(n, n)
    return array_encriptado, clave

def desencriptado(array_encriptado, clave):
    listadearray = array_encriptado.ravel().tolist()
    ordenado = []
    for i in range(len(listadearray)):
        posicion = clave.index(i)
        ordenado.append(chr(listadearray[posicion]))

    texto = "".join(ordenado)
    texto = texto.replace("_", "")

    return texto

a, b = encriptado('Today is Caturday!')
desencriptado(a, b)