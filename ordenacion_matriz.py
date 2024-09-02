def ordenar_fila_matriz(matriz, fila):
    matriz[fila].sort()
    return matriz

# Matriz bidimensional de ejemplo
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Fila a ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

# Llamada a la función de ordenación
matriz_ordenada = ordenar_fila_matriz(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
