#Comprobar el tipo de datos de una matriz
#Obtenga el tipo de datos de un objeto de matriz:
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

#Obtenga el tipo de datos de una matriz que contiene cadenas
import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)


#Crear matrices con un tipo de datos definido
#Creamos una matriz con tipo de datos cadena
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

#Creamos una matriz con tipo de datos entero de 4 bytes:
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)


#En caso de que un valor no se pueda convertir
#Si se proporciona un tipo en el que los elementos no se pueden convertir, NumPy generará un ValueError.
#ValueError: en Python, ValueError se genera cuando el tipo de argumento pasado a una función es inesperado/incorrecto
import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')


#Conversión de tipos de datos en matrices existentes
#Cambie el tipo de datos de flotante a entero usando 'i'como valor de parámetro
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

#Cambie el tipo de datos de flotante a entero usando intcomo valor de parámetro
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

#Cambie el tipo de datos de entero a booleano
import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)

