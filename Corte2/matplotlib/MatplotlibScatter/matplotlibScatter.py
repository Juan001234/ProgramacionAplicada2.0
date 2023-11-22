-------------------------------------------------------------------------------------------------------------Dispersión de Matplotlib-------------------------------------------------------------------------------------------------------------

____________________Creación de diagramas de dispersión____________________
#Con Pyplot, puede usar la función para dibujar un diagrama de dispersión.scatter()

#La función traza un punto para cada observación. Necesita dos matrices de la misma
#longitud, una para los valores de el eje x, y uno para los valores en el eje y:scatter()

----------Ejemplo 1:
#Un diagrama de dispersión simple:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

#La observación en el ejemplo anterior es el resultado del paso de 13 coches.

#El eje X muestra la antigüedad del coche.

#El eje Y muestra la velocidad del coche cuando pasa.

#¿Hay alguna relación entre las observaciones?

#Parece que cuanto más nuevo es el coche, más rápido conduce, pero eso podría ser una coincidencia, al fin y al cabo sólo matriculamos 13 coches.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Comparar Graficas____________________
#En el ejemplo anterior, parece haber una relación entre la velocidad y la edad, Pero, ¿y si también trazamos las observaciones de otro día?
#¿El diagrama de dispersión nos dirá algo más?

----------Ejemplo 2:
#Dibuja dos gráficos en la misma figura:
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()
#Nota: Los dos gráficos se trazan con dos colores diferentes, por defecto azul y naranja, aprenderá a cambiar los colores más adelante en este capítulo.

#Al comparar las dos gráficas, creo que es seguro decir que ambas nos dan la misma conclusión: cuanto más nuevo es el automóvil, más rápido conduce.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Colores____________________
#Puede establecer su propio color para cada diagrama de dispersión con el argumento o el argumento:colorc

----------Ejemplo 3:
#Establece tu propio color de los marcadores:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Colorea cada punto____________________
#Incluso puede establecer un color específico para cada punto utilizando una matriz de colores como valor para el argumento:c

#Nota: No se puede usar el argumento para esto, solo el argumento.colorc

----------Ejemplo 4:
#Establece tu propio color de los marcadores:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Mapa de colores____________________
#El módulo Matplotlib tiene una serie de mapas de colores disponibles.

#Un mapa de colores es como una lista de colores, donde cada color tiene un valor que varía de 0 a 100.

%%%%%Cómo usar el mapa de colores%%%%%
#Puede especificar el mapa de colores con el argumento de palabra clave con el valor del mapa de colores, en este que es uno de los mapas de colores incorporados disponibles en Matplotlib.cmap'viridis'

#Además, debe crear una matriz con valores (de 0 a 100), un valor para cada punto en el diagrama de dispersión:

----------Ejemplo 5:
#Cree una matriz de colores y especifique un mapa de colores en el diagrama de dispersión:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

#Puede incluir el mapa de colores en el dibujo incluyendo la instrucción:plt.colorbar()

----------Ejemplo 6:
#Incluya el mapa de colores real:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()

%%%%%Mapas de colores disponibles%%%%%
#Puede elegir cualquiera de los mapas de colores incorporados:
Name		 	  Reverse	
Accent		 	Accent_r	
Blues		 	  Blues_r	
BrBG		 	  BrBG_r	
BuGn		 	  BuGn_r	
BuPu		 	  BuPu_r	
CMRmap		 	CMRmap_r	
Dark2		 	  Dark2_r	
GnBu		 	  GnBu_r	
Greens		 	Greens_r	
Greys		 	  Greys_r	
OrRd		 	  OrRd_r	
Oranges		 	Oranges_r	
PRGn		 	  PRGn_r	
Paired		 	Paired_r	
Pastel1		 	Pastel1_r	
Pastel2		 	Pastel2_r	
PiYG		 	  PiYG_r	
PuBu		 	  PuBu_r	
PuBuGn		 	PuBuGn_r	
PuOr		 	  PuOr_r	
PuRd		 	  PuRd_r	
Purples		 	Purples_r	
RdBu		 	  RdBu_r	
RdGy		 	  RdGy_r	
RdPu		 	  RdPu_r	
RdYlBu		 	RdYlBu_r	
RdYlGn		 	RdYlGn_r	
Reds		 	  Reds_r	
Set1		 	  Set1_r	
Set2		 	  Set2_r	
Set3		 	  Set3_r	
Spectral		Spectral_r	
Wistia		 	Wistia_r	
YlGn		 	  YlGn_r	
YlGnBu		 	YlGnBu_r	
YlOrBr		 	YlOrBr_r	
YlOrRd		 	YlOrRd_r	
afmhot		 	afmhot_r	
autumn		 	autumn_r	
binary		 	binary_r	
bone		 	  bone_r	
brg		 	    brg_r	
bwr		 	    bwr_r	
cividis		  cividis_r	
cool		 	  cool_r	
coolwarm		coolwarm_r	
copper		 	copper_r	
cubehelix		cubehelix_r	
flag		 	  flag_r	
gist_earth	   gist_earth_r	
gist_gray		   gist_gray_r	
gist_heat		   gist_heat_r	
gist_ncar		   gist_ncar_r	
gist_rainbow	 gist_rainbow_r	
gist_stern		 gist_stern_r	
gist_yarg		 	 gist_yarg_r	
gnuplot		 	   gnuplot_r	
gnuplot2		 	 gnuplot2_r	
gray		 	     gray_r	
hot		 	      hot_r	
hsv		 	      hsv_r	
inferno		 	  inferno_r	
jet		 	      jet_r	
magma		 	    magma_r	
nipy_spectral		 	nipy_spectral_r	
ocean		 	        ocean_r	
pink		 	        pink_r	
plasma		 	plasma_r	
prism		 	prism_r	
rainbow		 	rainbow_r	
seismic		 	seismic_r	
spring		 	spring_r	
summer		 	summer_r	
tab10		 	tab10_r	
tab20		 	tab20_r	
tab20b		 	tab20b_r	
tab20c		 	tab20c_r	
terrain		 	terrain_r	
twilight		 	twilight_r	
twilight_shifted		 	twilight_shifted_r	
viridis		 	viridis_r	
winter		 	winter_r
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Tamaño____________________
#Puede cambiar el tamaño de los puntos con el argumento.s

#Al igual que los colores, asegúrese de que la matriz de tamaños tenga la misma longitud que las matrices de los ejes x e y:

----------Ejemplo 7:
Establezca su propio tamaño para los marcadores:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Alfa____________________
#Puede ajustar la transparencia de los puntos con el argumento.alpha

#Al igual que los colores, asegúrese de que la matriz de tamaños tenga la misma longitud que las matrices de los ejes x e y:

----------Ejemplo 8:
#Establezca su propio tamaño para los marcadores:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Combinar tamaño de color y alfa____________________
#Puede combinar un mapa de colores con diferentes tamaños de puntos. Esto se visualiza mejor si los puntos son transparentes:

----------Ejemplo 9:
#Cree matrices aleatorias con 100 valores para puntos x, puntos y, colores y Tamaños:
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
