-------------------------------------------------------------------------------------------------------------Marcadores Matplotlib-------------------------------------------------------------------------------------------------------------

____________________Marcadores____________________
#Puede usar el argumento de palabra clave para Enfatice cada punto con un marcador especificado:marker

----------Ejemplo 1:
#Marca cada punto con un círculo:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

----------Ejemplo 2:
#Marca cada punto con una estrella:
...
plt.plot(ypoints, marker = '*')
...
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Referencia de marcador____________________
#Puedes elegir cualquiera de estos marcadores:
Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Cadenas de formato fmt____________________
#También puede utilizar el parámetro de notación de cadena de acceso directo para especificar el marcador.

#Este parámetro también se llama , y se escribe con esta sintaxis:fmt

#marker|line|color

----------Ejemplo 3:
#Marca cada punto con un círculo:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()
#El valor del marcador puede ser cualquier cosa de la referencia de marcador anterior.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Referencia de línea____________________
#El valor de línea puede ser uno de los siguientes:
Line    Syntax	Description
'-'	    Solid line	
':'	    Dotted line	
'--'	  Dashed line	
'-.'	  Dashed/dotted line
#Nota: Si omite el valor de la línea en el parámetro fmt, no se trazará ninguna línea.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Referencia de color____________________
#El valor de color corto puede ser uno de los siguientes:
Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Tamaño del marcador____________________
#Puede utilizar el argumento de palabra clave o el argumento versión más corta, para establecer el tamaño de los marcadores:markersizems

----------Ejemplo 4:
#Establece el tamaño de los marcadores en 20:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Color del marcador____________________
#Puede utilizar el argumento de palabra clave o cuanto más corto sea para establecer el color del borde de los marcadores:markeredgecolormec

----------Ejemplo 5:
#Establezca el color de EDGE en rojo:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#Puede utilizar el argumento de palabra clave o el más corto para establecer el color dentro del borde de los marcadores:markerfacecolormfc

----------Ejemplo 6:
#Establece el color de la CARA en rojo:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

#Utilice los argumentos y para colorear todo el marcador:mecmfc

----------Ejemplo 7:
#Establece el color del borde y de la cara en rojo:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()

#También puede utilizar valores de color hexadecimales:

----------Ejemplo 8:
#Marca cada punto con un hermoso color verde:
...
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
...

#O cualquiera de los 140 nombres de color admitidos.

----------Ejemplo 9:
#Marca cada punto con el color llamado "hotpink":
...
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
...
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

