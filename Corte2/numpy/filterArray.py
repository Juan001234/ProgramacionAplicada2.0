-------------------------------------------------------------------------------------------------------------Matrices de filtrado-------------------------------------------------------------------------------------------------------------

____________________Matrices de filtrado____________________
#Obtener algunos elementos de una matriz existente y crear una nueva matriz de ellos se denomina filtrado.

#En NumPy, se filtra una matriz mediante una lista de índices booleanos.

#Nota: Una lista de índices booleanos es una lista de valores booleanos correspondientes a los índices de la matriz.

#Si el valor de un índice es que el elemento está contenido en la matriz filtrada,
#si el valor de ese índice es que el elemento se excluye de la matriz filtrada.TrueFalse

----------Ejemplo 1:
#Cree una matriz a partir de los elementos de los índices 0 y 2:
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
#El ejemplo anterior volverá, ¿por qué?[41, 43]

#Dado que la nueva matriz contiene solo los valores en los que la matriz de filtro tenía el valor, en este caso, index 0 y 2.True
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Creación de la matriz de filtros____________________
#En el ejemplo anterior, codificamos de forma rígida los valores and, pero el uso común es crear una matriz de filtros basada en condiciones.TrueFalse

----------Ejemplo 2:
#Cree una matriz de filtros que devuelva solo valores superiores a 42:
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

----------Ejemplo 3:
#Cree una matriz de filtros que devuelva solo elementos pares del original arreglo:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Creación de filtros directamente desde la matriz____________________
#El ejemplo anterior es una tarea bastante común en NumPy y NumPy proporciona una buena manera de abordarla.

#Podemos sustituir directamente la matriz en lugar de la variable iterable en nuestra condición y funcionará tal como esperamos.

----------Ejemplo 4:
#Cree una matriz de filtros que devuelva solo valores superiores a 42:
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

----------Ejemplo 5:
#Cree una matriz de filtros que devuelva solo elementos pares del original arreglo:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


