#Crea un array con valores en grados centígrados y conviértelos a Fahrenheit. fahrenheit = (celsius * 9/5) + 32.

# Importamos la librería numpy
import numpy as np

# Creamos el array
array = np.array([0, 12, 45.21 ,34, 99.91])

# Convertimos los grados centígrados a grados Fahrenheit
arrayFahrenheit = (array * 9/5) + 32

# Mostramos el array
print("Array de grados centígrados: ")
print(array)
print("Array de grados Fahrenheit: ")
print(arrayFahrenheit)