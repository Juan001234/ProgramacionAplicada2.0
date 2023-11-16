#Introdiccion a numpy
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr) #arreglo simple con libreria numpy

#Importar numpy con apodo
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

#verificar version de numpy
import numpy as np

print(np.__version__)


#Crear un objeto NumPy ndarray
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
#type(): esta función incorporada de Python nos dice el tipo de objeto que se le pasa. Como en el código anterior, muestra que arres numpy.ndarraytipo.


#Utilizamos una tupla para crear una matriz NumPy
import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)


#Dimensiones en matrices
#son matrices que tienen matrices como elementos.

#Matrices 0-D
import numpy as np

arr = np.array(42)

print(arr) #una matriz 0-D con valor 42

#Matrices 1-D
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr) #una matriz 1-D que contenga los valores 1,2,3,4,5

#Matrices 2-D
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr) #una matriz 2-D que contenga dos matrices con los valores 1,2,3 y 4,5,6

#Matrices 3-D
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr) #una matriz 3D con dos matrices 2D, ambas conteniendo dos matrices con los valores 1,2,3 y 4,5,6


#Verificar número de dimensiones
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim) #Comprueba cuantas dimensiones tiene la matriz

#Matrices de dimensiones superiores
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim) #Una mateiz de 5 dimensiones y que verifica cuantas dimensiones tiene



#Acceder a elementos de matriz
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0]) #Obtiene el primer elemento de la siguiente matriz

#Obtiene el tercer y cuarto elemento de la siguiente matriz y los suma
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

#Acceder a matrices 2-D
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1]) Accede al elemento en la primera fila, segunda columna

#Acceda a matrices 3-D
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2]) #Accede al tercer elemento de la segunda matriz de la primera matriz

#explicacion:
#arr[0, 1, 2]imprime el valor 6.

#Y es por esto:

#El primer número representa la primera dimensión, que contiene dos matrices:
#[[1, 2, 3], [4, 5, 6]]
#y:
#[[7, 8, 9], [10, 11, 12]]
#Desde seleccionamos 0, nos queda el primer array:
#[[1, 2, 3], [4, 5, 6]]

#El segundo número representa la segunda dimensión, que también contiene dos matrices:
#[1, 2, 3]
#y:
#[4, 5, 6]
#Como seleccionamos 1, nos queda la segunda matriz:
#[4, 5, 6]

#El tercer número representa la tercera dimensión, que contiene tres valores:
#4
#5
#6
#Como seleccionamos 2, terminamos con el tercer valor:
#6


#Indexación negativa
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1]) #Utiliza indexación negativa para acceder a una matriz desde el final


#Corte de matriz NumPy
# En ptython Cortar significa tomar elementos de un índice determinado a otro índice determinado.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) #Corte elementos del índice 1 al índice 5
#impoertante:El resultado incluye el índice inicial, pero excluye el índice final.

#Cortar elementos desde el índice 4 hasta el final de la matriz
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

#Cortar elementos desde el principio hasta el índice 4 (no incluido)
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])


#Rebanado negativo
#Utilice el operador menos para hacer referencia a un índice desde el final
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])



#STEP
#Utilice el valor STEP para determinar el paso del corte
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) #Devuelve todos los demás elementos del índice 1 al índice 5

#Devolver todos los demás elementos de toda la matriz
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])


#Cortar matrices 2-D
#Desde el segundo elemento, corta los elementos del índice 1 al índice 4 (no incluido)
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4]) #recordar que el segundo elemento tiene índice 1

#De ambos elementos, devuelve el índice 2:
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])

#De ambos elementos, divida el índice 1 al índice 4 (no incluido), esto devolverá una matriz 2-D:
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
