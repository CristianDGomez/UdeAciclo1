valorunitario = float(input("Ingese el valor unitario: "))
pregunta1 = input("¿El producto cuenta con IVA?: ")
subtotal = 0
if pregunta1 == "S":
    nc = int(input("Ingrese la cantidad que lleva el cliente del producto a registrar: "))
    print("IVA incluido")
    subtotal = valorunitario * nc + 0.19 * valorunitario * nc
    print(f"subtotal: {subtotal}")
elif pregunta1 == "N":
    nc = int(input("Ingrese la cantidad que lleva el cliente del producto a registrar: "))
    print("PRODUCTO SIN IVA")
    subtotal = valorunitario * nc
    print(f"subtotal: {subtotal}")

pregunta2 = input("¿Faltan productos por cobrar? S/N: ")
condicion = (pregunta2 == "S")
while condicion == True:

    valorunitario =float(input("Ingrese el valor unitario: "))
    pregunta3 = input("¿El producto cuenta con IVA: ")
    if pregunta3 == "S":
        nc = int(input("Ingrese la cantidad que lleva el cliente del producto: "))
        print("IVA incluido")
        subtotal = valorunitario * nc + 0.19 * valorunitario * nc + subtotal
        print(f"subtotal: {subtotal}")
    elif pregunta3 == "N":
        nc = int(input("Ingrese la cantidad que lleva el cliente del producto: "))
        print("PRODUCTO SIN IVA")
        subtotal = valorunitario * nc + subtotal
        print(f"subtotal: {subtotal}")

    pregunta2 = input("¿Faltan productos por cobrar? S/N: ")
    condicion = (pregunta2 == "S")

else:
    total = subtotal
    print(f"TOTAL: {total}")
