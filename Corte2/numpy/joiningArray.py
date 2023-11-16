--------------------------------------------------------------------------------------------Matriz de unión NumPy--------------------------------------------------------------------------------------------------------------------------------------

____________________Unión de matrices NumPy____________________
#Unir significa poner el contenido de dos o más matrices en una sola matriz.

#En SQL unimos tablas en base a una clave, mientras que en NumPy unimos matrices por ejes.

#Pasamos una secuencia de matrices que queremos unir a la función, junto con el eje. Si axis no se pasa explícitamente, se toma como 0.concatenate()

----------Ejemplo 1:
#Unir dos matrices:
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

----------Ejemplo 2:
#Unir dos matrices 2D a lo largo de las filas (eje = 1):
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Unión de matrices mediante funciones de pila____________________
#El apilamiento es lo mismo que la concatenación, la única diferencia es que el apilamiento se realiza a lo largo de un nuevo eje.

#Podemos concatenar dos matrices 1-D a lo largo del segundo eje, lo que daría como resultado ponerlas una encima el otro, es decir. apilamiento.

#Pasamos una secuencia de matrices que queremos unir al método junto con el eje. Si axis no se pasa explícitamente, se toma como 0.stack()


----------Ejemplo 3:
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Apilamiento a lo largo de columnas____________________
#NumPy proporciona una función auxiliar: apilar a lo largo de columnas.vstack()

----------Ejemplo 4:
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Apilamiento a lo largo de la altura (profundidad)____________________
#NumPy proporciona una función auxiliar: apilar a lo largo de la altura, que es lo mismo que la profundidad.dstack()

----------Ejemplo 5:
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
