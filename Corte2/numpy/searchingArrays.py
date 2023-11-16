-------------------------------------------------------------------------------------------------------------Matrices de búsqueda de NumPy-------------------------------------------------------------------------------------------------------------

____________________Búsqueda de matrices____________________
#Puede buscar un valor determinado en una matriz y devolver los índices que obtienen una coincidencia.

#Para buscar en una matriz, utilice el método.where()

----------Ejemplo 1:
#Encuentre los índices en los que el valor es 4:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)


#El ejemplo anterior devolverá una tupla: (array([3, 5, 6],)

#Lo que significa que el valor 4 está presente en los índices 3, 5 y 6.

----------Ejemplo 2:
#Encuentre los índices en los que los valores son pares:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)


----------Ejemplo 3:
#Encuentre los índices en los que los valores son impares: 
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Buscar ordenado____________________
#Hay un método llamado que realiza una búsqueda binaria en la matriz, y devuelve el índice en el que se insertaría el valor especificado
#para mantener el valor Orden de búsqueda.searchsorted()

#Se supone que el método es Se utiliza en matrices ordenadas.searchsorted()

----------Ejemplo 4:
Encuentre los índices en los que se debe insertar el valor 7:
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
#Ejemplo explicado: El número 7 debe insertarse en el índice 1 para mantener el criterio de ordenación.

#El método inicia la búsqueda desde la izquierda y devuelve el primer índice donde el número 7 ya no es mayor que el siguiente valor.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

////Buscar desde el lado derecho\\\\
#De forma predeterminada, se devuelve el índice situado más a la izquierda, pero podemos dar para devolver el índice situado más a la derecha en su lugar.side='right'

----------Ejemplo 5:
Encuentre los índices en los que se debe insertar el valor 7, a partir de la Derecha:
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)
#Ejemplo explicado: El número 7 debe insertarse en el índice 2 para mantener el criterio de ordenación.

#El método inicia la búsqueda desde la derecha y devuelve el primer índice donde el número 7 ya no es menor que el siguiente valor.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

////Valores múltiples\\\\
#Para buscar más de un valor, utilice una matriz con los valores especificados.

----------Ejemplo 6:
Encuentre los índices donde se deben insertar los valores 2, 4 y 6:
import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)
#El valor devuelto es una matriz: contiene los tres índices donde se insertarían 2, 4, 6 en la matriz original para mantener el orden.[1 2 3] 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
