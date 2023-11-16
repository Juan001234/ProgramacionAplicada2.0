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
