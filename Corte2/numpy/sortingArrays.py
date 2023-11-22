-------------------------------------------------------------------------------------------------------------Matrices de clasificación de NumPy-------------------------------------------------------------------------------------------------------------
____________________Matrices de clasificación____________________
#Ordenar significa poner elementos en una secuencia ordenada.

#La secuencia ordenada es cualquier secuencia que tiene un orden correspondiente a elementos, como numérico o alfabético, ascendente o descendente.

#El objeto ndarray NumPy tiene una función llamada , que ordenará una matriz especificada.sort()

----------Ejemplo 1:
#Ordene la matriz:
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))
#Nota: Este método devuelve una copia de la matriz, dejando el matriz original sin cambios.

#También puede ordenar matrices de cadenas o cualquier otro tipo de datos:

----------Ejemplo 2:
#Ordene la matriz alfabéticamente:
import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

----------Ejemplo 3:
#Ordene una matriz booleana:
import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Ordenar una matriz 2D____________________
#Si utiliza el método sort() en una matriz 2D, ambas matrices se ordenarán:

----------Ejemplo 4:
#Ordenar una matriz 2D:
import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

