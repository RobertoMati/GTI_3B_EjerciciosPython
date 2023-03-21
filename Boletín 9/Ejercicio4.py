#Crea una matriz de 8x8 con un patrón de tablero de ajedrez (0's y 1's).

# Importamos la librería numpy
import numpy as np

# Creamos la matriz
matriz = np.zeros((8,8))

# Añadimos los 1's 
matriz[1::2,::2] = 1 # Filas impares, columnas pares. 
#Con 1::2, empezamos en la fila 1 y vamos de 2 en 2. Con ::2, empezamos en la columna 0 y vamos de 2 en 2.

# Mostramos la matriz
print(matriz)