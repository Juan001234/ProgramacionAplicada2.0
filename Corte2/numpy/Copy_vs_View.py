#La principal diferencia entre una copia y una vista de una matriz es que la copia es una nueva matriz y la vista es solo una vista de la matriz original

#Copy
#Haga una copia, cambie la matriz original y muestre ambas matrices
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#View
#Cree una vista, cambie la matriz original y muestre ambas matrices
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

#Realizar cambios en View
#Cree una vista, cambie la vista y muestre ambas matrices
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)


#Compruebe si Array posee sus datos
#Imprima el valor del atributo base para verificar si una matriz posee sus datos o no
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
