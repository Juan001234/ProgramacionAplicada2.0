-------------------------------------------------------------------------------------------------------------Barras de Matplotlib-------------------------------------------------------------------------------------------------------------

____________________Creación de barras____________________
#Con Pyplot, puede usar la función Para dibujar gráficos de barras:bar()

----------Ejemplo 1:
#Dibuja 4 barras:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#La función toma argumentos que describen el disposición de las barras.bar()

#Las categorías y sus valores representados por el primer y segundo argumento como matrices.

----------Ejemplo 2:

x = ["APPLES", "BANANAS"]
y = [400, 350]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Barras horizontales____________________
#Si desea que las barras se muestren horizontalmente en lugar de verticalmente, Utilice la función:barh()

----------Ejemplo 2:
#Dibuja 4 barras horizontales:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Color de la barra____________________
 #El y tome el argumento de la palabra clave para establecer el color de las barras:bar()barh()color
 ----------Ejemplo 3:
#Dibuja 4 barras rojas:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Nombres de colores____________________
#Puede utilizar cualquiera de los 140 nombres de color admitidos.

----------Ejemplo 4:
#Dibuja 4 barras de color "rosa intenso":
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Hexágono de color____________________
#O bien, puede usar valores de color hexadecimales:

----------Ejemplo 5:
#Dibuja 4 barras con un hermoso color verde:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Ancho de la barra____________________
#Toma el argumento de la palabra clave para establecer el ancho de las barras:bar()width

----------Ejemplo 6:
#Dibuja 4 barras muy finas:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()
#El valor de ancho predeterminado es 0,8

#Nota: Para barras horizontales, use en lugar de .heightwidth

____________________Altura de la barra____________________
#Toma el argumento de la palabra clave para establecer la altura de las barras:barh()height

----------Ejemplo 7:
#Dibuja 4 barras muy finas:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()
#El valor de altura predeterminado es 0,8
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
