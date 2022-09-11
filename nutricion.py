# Peso de ganancia por tipo de alimento.
# Carbohidratos: 60.1 g de peso.
# Frutas y verduras: 24.4 g de peso.
# proteina: 30.5g de peso.

def solucion(edad, peso):
    edad = int(input('Ingrese la edad del paciente: '))
    peso = float(input('Ingrese el peso del paciente en kilogramos: '))

    kc = 60.1/1000
    kp = 30.5/1000
    kv = 24.4/1000

    if edad >= 5 and edad <= 10:
        if peso < 16:
            estadoNutricional = "A"
            pesoObjetivo = 22
        elif peso > 28:
            estadoNutricional = "B"
            pesoObjetivo = 24
        elif peso < 28:
            estadoNutricional = "C"
            pesoObjetivo = 28
    if edad > 10 and edad <= 13:
        if peso < 30:
            estadoNutricional = "A"
            pesoObjetivo = 32
        elif peso > 50:
            estadoNutricional = "B"
            pesoObjetivo = 43
        elif peso < 50:
            estadoNutricional = "C"
            pesoObjetivo = 50
    if edad > 13 and edad <= 17:
        if peso < 51:
            estadoNutricional = "A"
            pesoObjetivo = 56
        elif peso > 63:
            estadoNutricional = "B"
            pesoObjetivo = 58
        elif peso < 63:
            estadoNutricional = "C"
            pesoObjetivo = 63
    if estadoNutricional == "A":
        pc = 2
        pp = 1
        pv = 2
        mensaje = "un peso saludable"
        k = 0
    elif estadoNutricional == "B":
        pc = 0.6
        pp = 1
        pv = 4
        mensaje = "un peso saludable"
        k = 1
    elif estadoNutricional == "C":
        pc = 0.5
        pp = 0.7
        pv = 2
        mensaje = "maximo"
    if peso > 55:
        k = 0
    else:
        k = 1
    aporteNutricional = abs(kc*pc+kp*pp-kv*pv)
    pesoCompensar = abs(pesoObjetivo-peso)
    dias = int(round(pesoCompensar/aporteNutricional,0))+k
    print(f'El estado nutricional del paciente es {estadoNutricional} y se requiere {dias} dias de dieta para que alcance {mensaje}')

solucion(0,0)