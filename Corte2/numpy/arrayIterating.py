--------------------------------------------------------------------------Iteración de matrices NumPy----------------------------------------------------------------------------------------------------------------------

____________________Iteración de matrices____________________
#Iterar significa ir a través de los elementos uno por uno.

#Como tratamos con matrices multidimensionales en numpy, podemos hacer esto usando el bucle básico de python.for

#Si iteramos en una matriz 1-D, pasará por cada elemento uno por uno.

----------Ejemplo 1:
#Iterar en los elementos de la siguiente matriz 1D:
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Iteración de matrices 2D____________________
#En una matriz 2-D, pasará por todas las filas.

----------Ejemplo 2:
#Itere en los elementos de la siguiente matriz 2D:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)
#Nota: Si iteramos en una matriz n-D, pasará por la dimensión n-1 una por una.

#Para devolver los valores reales, los escalares, tenemos que iterar las matrices en cada dimensión.

----------Ejemplo 3:
Iterar en cada elemento escalar de la matriz 2D:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Iteración de matrices 3D____________________
#En una matriz 3D, pasará por todas las matrices 2D.

----------Ejemplo 4:
Itere en los elementos de la siguiente matriz 3D:
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)
  
#Para devolver los valores reales, los escalares, tenemos que iterar las matrices en cada dimensión.

----------Ejemplo 5:
#Iterar hasta los escalares:
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Iteración de matrices usando nditer()____________________
#La función es una función de ayuda que se puede utilizar desde iteraciones muy básicas hasta muy avanzadas. Resuelve algunos problemas básicos a los que nos
#enfrentamos en la iteración, vamos a repasarlo con ejemplos. nditer()

----Iteración en cada elemento escalar---
#En bucles básicos, iterando a través de cada escalar de una matriz, necesitamos usar n bucles que pueden ser difíciles de escribir para matrices con muy alta dimensionalidad.for for

----------Ejemplo 6:
#Iterar a través de la siguiente matriz 3D:
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Iteración de matrices con diferentes tipos de datos____________________
#Podemos usar el argumento y pasarle el tipo de datos esperado para cambiar el tipo de datos de los elementos mientras itera.op_dtypes

#NumPy no cambia el tipo de datos del elemento in situ (donde el elemento está en la matriz) por lo que necesita algún otro espacio para realizar esta acción, ese
#espacio extra se llama buffer, y para habilitarlo pasamos .nditer()flags=['buffered']

----------Ejemplo 7:
#Iterar a través de la matriz como una cadena:
import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Iteración con diferentes tamaños de paso____________________
#Podemos usar el filtrado y seguido de la iteración.

----------Ejemplo 8:
#Iterar a través de cada elemento escalar de la matriz 2D omitiendo 1 elemento:
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


____________________Iteración enumerada usando ndenumerate()____________________
#Enumeración significa mencionar el número de secuencia de algo uno por uno.

#A veces requerimos el índice correspondiente del elemento mientras iteramos, el método se puede usar para esos casos de uso.ndenumerate()

----------Ejemplo 9:
#Enumere los siguientes elementos de matrices 1D:
import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

----------Ejemplo 10:
#Enumere los siguientes elementos de la matriz 2D:
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



