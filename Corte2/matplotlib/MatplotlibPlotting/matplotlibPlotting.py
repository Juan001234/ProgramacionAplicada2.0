-------------------------------------------------------------------------------------------------------------Trazado de Matplotlib-------------------------------------------------------------------------------------------------------------

____________________Trazar los puntos x e y____________________
#La función se utiliza para dibujar puntos (marcadores) en un diagrama.plot()

#De forma predeterminada, la función dibuja una línea de punto a punto.plot()

#La función toma parámetros para especificar puntos en el diagrama.

#El parámetro 1 es una matriz que contiene los puntos del eje x.

#El parámetro 2 es una matriz que contiene los puntos del eje Y.

#Si necesitamos trazar una línea de (1, 3) a (8, 10), tenemos que pasar dos matrices [1, 8] y [3, 10] a la función plot.

----------Ejemplo 1:
#Dibuja una línea en un diagrama desde la posición (1, 3) hasta la posición (8, 10):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
#El eje x es el eje horizontal.

#El eje Y es el eje vertical.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Trazado sin línea____________________
#Para trazar solo los marcadores, puede usar el parámetro de notación de cadena de acceso directo 'o', que significa 'anillos'.

----------Ejemplo 2:
#Dibuja dos puntos en el diagrama, uno en la posición (1, 3) y otro en la posición (8, 10):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Múltiples puntos____________________
#Puedes trazar tantos puntos como quieras, solo asegúrate de tener el mismo número de puntos en ambos ejes.

----------Ejemplo 3:
#Dibuja una línea en un diagrama desde la posición (1, 3) hasta (2, 8), luego hasta (6, 1) y finalmente hasta la posición (8, 10):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Puntos X predeterminados____________________
#Si no especificamos los puntos en el eje x, obtendrán los valores predeterminados 0, 1, 2, 3, etc., dependiendo de la longitud de los puntos y.

#Entonces, si tomamos el mismo ejemplo anterior y dejamos de lado los puntos x, el diagrama se verá así:

----------Ejemplo 4:
#Trazar sin puntos x:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
#Nota: Los puntos x en el ejemplo anterior son [0, 1, 2, 3, 4, 5].
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
