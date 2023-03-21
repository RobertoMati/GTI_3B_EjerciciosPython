#Crea un array con los valores de 10 a 20 e inviértelos en un nuevo array.

# Importamos la librería numpy
import numpy as np

# Creamos el array
array = np.arange(10,21)

# Invertimos el array
arrayInvertido = array[::-1]

# Mostramos el array
print(array)
print(arrayInvertido)