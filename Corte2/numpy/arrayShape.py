#Obtener la forma de una matriz
#Imprime la forma de una matriz 2D:
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) 
#El ejemplo anterior devuelve , lo que significa que la matriz tiene 2 dimensiones, donde la primera dimensión tiene 2 elementos y la segunda tiene 4.(2, 4)

#Cree una matriz con 5 dimensiones utilizando un vector con valores 1,2,3,4 y verifique que la última dimensión tenga el valor 4:ndmin
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

#Definición importante de w3schools
#¿Qué representa la tupla de forma?
#Los enteros de cada índice indican el número de elementos que tiene la dimensión correspondiente.

#En el ejemplo anterior en el índice-4 tenemos el valor 4, por lo que podemos decir que la 5ª dimensión (4 + 1ª) tiene 4 elementos.
