-------------------------------------------------------------------------------------------------------------Línea Matplotlib-------------------------------------------------------------------------------------------------------------

____________________Estilo de línea____________________
#Puede usar el argumento de palabra clave , o más corto , para Cambie el estilo de la línea trazada:linestylels

----------Ejemplo 1:
#Usa una línea punteada:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

----------Ejemplo 2:
#Usa una línea discontinua:
plt.plot(ypoints, linestyle = 'dashed')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Sintaxis más corta____________________
#El estilo de línea se puede escribir en una sintaxis más corta:

#linestyle se puede escribir como .ls

#dotted se puede escribir como .:

#dashed se puede escribir como .--


----------Ejemplo 3:
#Sintaxis más corta:
plt.plot(ypoints, ls = ':')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Estilos de línea____________________
#Puedes elegir cualquiera de estos estilos:
Style	            Or
'solid'(default)	'-'	
'dotted'	        ':'	
'dashed'	        '--'	
'dashdot'	        '-.'	
'None'	          '' or ' '	
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Color de la línea____________________
#Puede utilizar el argumento de palabra clave o el más corto para establecer el color de la línea:colorc

----------Ejemplo 4:
#Establece el color de la línea en rojo:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

#También puede utilizar valores de color hexadecimales:

----------Ejemplo 5:
#Parcela con una bonita línea verde:
...
plt.plot(ypoints, c = '#4CAF50')
...

#O cualquiera de los 140 nombres de color admitidos.

----------Ejemplo 6:
#Gráfico con el color llamado "hotpink":
...
plt.plot(ypoints, c = 'hotpink')
...
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Ancho de línea____________________
#Puede utilizar el argumento de palabra clave o cuanto más corto sea para cambiar el ancho de la línea.linewidthlw

#El valor es un número flotante, en puntos:

----------Ejemplo 6:
#Gráfico con una línea ancha de 20,5 puntos:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Múltiples líneas____________________
#Puedes trazar tantas líneas como quieras simplemente añadiendo más funciones:plt.plot()

----------Ejemplo 7:
#Dibuje dos líneas especificando una función para cada línea:plt.plot()
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

#También puede trazar muchas líneas sumando los puntos de los ejes x e y para cada línea en la misma función.plt.plot()

#(En los ejemplos anteriores, solo especificamos los puntos en el eje y, lo que significa que los puntos
#en el eje x obtuvieron los valores predeterminados (0, 1, 2, 3).)

#Los valores x e y vienen en pares:

----------Ejemplo 8:
#Dibuje dos líneas especificando los valores de los puntos x e y para ambas líneas:
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
