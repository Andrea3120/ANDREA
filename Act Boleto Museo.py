
"""Boleto Museo"""

print("Boletos museo")
numvis = int(input("Ingrese número de visitantes: "))
total = 0  # Para acumular el total

for i in range(numvis):
    edadvis = int(input(f"Edad de visitante {i+1}: "))

    if edadvis <= 3:
        print("¡Eres un bebé! Pasas gratis ")
        continue
    elif edadvis <= 18:
        precio_base = 30
        print("Tienes un descuento de adolescente")
    else:
        precio_base = 45

    tipo = input("¿Eres un Adulto Mayor, Profesor o Estudiante? ").lower()

    if tipo == "adulto mayor":
        descuento = 0.12
    elif tipo == "profesor":
        descuento = 0.10
    elif tipo == "estudiante":
        descuento = 0.10
    else:
        descuento = 0

    precio_final = precio_base * (1 - descuento)
    print(f"Este es tu precio final: ${precio_final:.2f}")

    total += precio_final

print(f"\nTotal a pagar por todos los boletos: ${total:.2f}")
