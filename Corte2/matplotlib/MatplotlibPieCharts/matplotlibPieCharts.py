-------------------------------------------------------------------------------------------------------------Gráficos circulares de Matplotlib-------------------------------------------------------------------------------------------------------------

____________________Creación de gráficos circulares____________________
#Con Pyplot, puede usar la función Para dibujar gráficos circulares:pie()

----------Ejemplo 1:
#Un gráfico circular simple:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()
#el gráfico circular dibuja una pieza (llamada cuña) para cada valor en la matriz (en este caso [35, 25, 25, 15]).

#De forma predeterminada, el trazado de la primera cuña comienza desde el eje x y se mueve en sentido contrario a las agujas del reloj

#Nota: El tamaño de cada cuña se determina comparando el valor con todos los demás valores, utilizando esta fórmula:
#El valor dividido por la suma de todos los valores: x/sum(x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Etiquetas____________________
#Agregue etiquetas al gráfico circular con el parámetro.label

#El parámetro debe ser una matriz con una etiqueta para cada cuña:label

----------Ejemplo 2:
#Un gráfico circular simple:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Ángulo de inicio____________________
#Como se mencionó, el ángulo de inicio predeterminado está en el eje x, pero puede cambiar el ángulo de inicio especificando un parámetro.startangle

#El parámetro se define con un ángulo en grados, el ángulo predeterminado es 0:startangle

----------Ejemplo 3:
#Comience la primera cuña a 90 grados:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Explode____________________
#¿Quizás quieres que una de las cuñas se destaque? El parámetro le permite hacer eso.explode

#El parámetro, si se especifica, y no , Debe ser una matriz con un valor para cada cuña.explodeNone

#Cada valor representa la distancia desde el centro a la que se muestra cada cuña:

----------Ejemplo 4:
#Tira de la cuña de "Manzanas" 0.2 desde el centro del "pastel":
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Sombra____________________
#Agregue una sombra al gráfico circular estableciendo el parámetro en :shadowsTrue

----------Ejemplo 5:
#Añade una sombra:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Colores____________________
#Puede establecer el color de cada cuña con el parámetro.colors

#El parámetro, si se especifica, Debe ser una matriz con un valor para cada cuña:colors

----------Ejemplo 6:
#Especifique un nuevo color para cada cuña:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

#Puede utilizar valores de color hexadecimales, cualquiera de los 140 nombres de color admitidos, o uno de estos atajos:

'r' - Rojo
- Verde
- Azul
- Cian
- Magenta
- Amarillo - Negro
- Blanco
'g''b''c''m''y''k''w'
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Leyenda____________________
#Para agregar una lista de explicaciones para cada cuña, use la función:legend()
----------Ejemplo 7:
#Añade una leyenda:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Leyenda con encabezado____________________
#Para agregar un encabezado a la leyenda, agregue el parámetro a la función.titlelegend

----------Ejemplo 8:
#Agregue una leyenda con un encabezado:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
