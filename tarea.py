# Ejercicio: Sumar todos los elementos de una matriz
matriz = [
    [1, 2, 3],  # Fila 1
    [4, 5, 0],  # Fila 2
    [2, 2, 2]   # Fila 3
]

suma_total = 0

for fila in matriz:
    
    for elemento in fila:
        suma_total += elemento

print("La suma de todos los elementos de la matriz es:", suma_total)