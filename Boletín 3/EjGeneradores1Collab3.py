#Escribe una función generadora de la secuencia de Fibonacci y comprueba su correcto funcionamiento. 
#Los valores de esta secuencia se calculan siguiendo la siguiente fórmula:
"""                                      F0=0
                                         F1=1
                                   Fn=Fn−1+Fn−2 ∀n>1
"""

def fibonacci():
      f0, f1 = 0, 1
      while True:
            yield f0
            f0, f1 = f1, f0 + f1

for i in fibonacci():
      if i > 100:
            break
      print(i)
    