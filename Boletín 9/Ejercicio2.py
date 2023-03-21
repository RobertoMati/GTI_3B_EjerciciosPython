#Crea una matriz de 10x10 con 1's en los bordes y 0's en el interior.

# Importamos la librería numpy
import numpy as np

# Creamos la matriz
matriz = np.ones((10,10))

# Creamos la matriz
matriz[1:-1,1:-1] = 0

# Mostramos la matriz
print(matriz)

