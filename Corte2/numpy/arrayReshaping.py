--------------------------------------------------------------------------Remodelación de matrices NumPy--------------------------------------------------------------------------------------------------------------------

____________________Cambiar la forma de 1D a 2D____________________

----------Ejemplo 1:
#Convierta la siguiente matriz 1D con 12 elementos en una matriz 2D.
#La dimensión más externa tendrá 4 matrices, cada una con 3 elementos
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Cambiar la forma de 1D a 3D____________________
----------Ejemplo 2:
#Convierta la siguiente matriz 1D con 12 elementos en una matriz 3D.
#La dimensión más externa tendrá 2 matrices que contienen 3 matrices, cada una con 2 elementos
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________¿Podemos remodelar en cualquier forma?____________________

#Podemos remodelar en cualquier forma siempre y cuando los elementos necesarios para la remodelación sean iguales en ambas formas.
#Podemos remodelar una matriz 1D de 8 elementos en una matriz 2D de 4 elementos en 2 filas, pero no podemos remodelarla en una matriz 2D de 3 elementos y 3 filas, ya que requeriría 3x3 = 9 elementos.

----------Ejemplo 3:
Intente convertir una matriz 1D con 8 elementos en una matriz 2D con 3 elementos en cada dimensión (generará un error):
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)

print(newarr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________________¿Devoluciones Copy or View?____________________________ 
----------Ejemplo 4:
Compruebe si la matriz devuelta es una copia o una vista:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________________¿Dimensión desconocida?____________________________ 
#Se te permite tener una dimensión "desconocida".

#Lo que significa que no tiene que especificar un número exacto para uno de los dimensiones en el método de remodelación.

#Pase como el valor, y NumPy Calcula este número por ti.-1


----------Ejemplo 5:
Convierta una matriz 1D con 8 elementos en una matriz 3D con elementos 2x2:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)
#Nota: No podemos pasar a más de una dimensión.-1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________________Aplanamiento de las matrices____________________________ 
#Aplanar una matriz significa convertir una matriz multidimensional en una matriz 1D.

#Podemos usar para hacer esto.reshape(-1)

----------Ejemplo 6:
Convierta la matriz en una matriz 1D:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Nota: Hay muchas funciones para cambiar las formas de las matrices en numpy , y también para reorganizar los elementos , , , etc. Estos se incluyen en la sección Intermedio a Avanzado de numpy.flatten ravel rot90 flip fliplr flipud      
