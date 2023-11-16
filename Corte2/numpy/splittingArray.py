-----------------------------------------------------------------------------------------------Matriz de división NumPy-----------------------------------------------------------------------------------------------------------------------------------------

____________________División de matrices NumPy____________________
#La división es una operación inversa de la unión.

#La unión fusiona varias matrices en una sola y la división rompe una matriz en múltiplos.

#Usamos para dividir arrays, le pasamos el array que queremos dividir y el número de divisiones.array_split()

----------Ejemplo 1:
Divida la matriz en 3 partes:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
#Nota: El valor devuelto es una lista que contiene tres matrices.

#Si la matriz tiene menos elementos de los necesarios, se ajustará desde el final en consecuencia.


----------Ejemplo 2:
#Divida la matriz en 4 partes:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

#Nota: También tenemos el método disponible, pero no ajustará los elementos cuando los elementos estén menos en source para dividir como en el ejemplo anterior, funcionaba correctamente pero fallaba.split()array_split()split()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Dividir en matrices____________________
#El valor devuelto del método es una matriz que contiene cada una de las divisiones como una matriz.array_split()

#Si divide una matriz en 3 matrices, puede acceder a ellas desde el resultado como cualquier elemento de matriz:

----------Ejemplo 3:
#Acceda a las matrices divididas:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________División de matrices 2D____________________
#Utilice la misma sintaxis al dividir matrices 2D.

#Use el método, pase la matriz tú quieres dividir y el número de divisiones que quieres hacer.array_split()

----------Ejemplo 4:
Divida la matriz 2D en tres matrices 2D:
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)
      
      
#En el ejemplo anterior se devuelven tres matrices 2D.

#Veamos otro ejemplo, esta vez cada elemento de las matrices 2D Contiene 3 elementos.

----------Ejemplo 5:
#Divida la matriz 2D en tres matrices 2D
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)
      

#En el ejemplo anterior se devuelven tres matrices 2D.

#Además, puede especificar alrededor de qué eje desea hacer la división.

#El siguiente ejemplo también devuelve tres matrices 2D, pero se dividen a lo largo de la fila (eje=1).

----------Ejemplo 6:      
#Divida la matriz 2D en tres matrices 2D a lo largo de filas:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)


#Una solución alternativa es usar lo opuesto a hsplit()hstack()

----------Ejemplo 7:   
#Utilice el método para dividir la matriz 2D en tres matrices 2D a lo largo de filas.hsplit()
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%      
