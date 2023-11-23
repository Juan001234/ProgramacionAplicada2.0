-------------------------------------------------------------------------------------------------------------Histogramas de Matplotlib-------------------------------------------------------------------------------------------------------------

____________________Histograma____________________
#Un histograma es un gráfico que muestra las distribuciones de frecuencia.

#Es un gráfico que muestra el número de observaciones dentro de cada intervalo dado.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Crear histograma____________________
#En Matplotlib, usamos la función para Crear histogramas.hist()

#La función usará una matriz de números para crear un histograma, la matriz se envía a la función como un argumento.hist()

#Para simplificar, usamos NumPy para generar aleatoriamente una matriz con 250 valores, donde los valores se concentrarán alrededor
#de 170, y la desviación estándar es 10. Más información sobre los datos normales Distribución en nuestro Machine Learning Tutorial.

----------Ejemplo 1:
#Una distribución normal de datos por NumPy:
import numpy as np

x = np.random.normal(170, 10, 250)

print(x)

#La función leerá la matriz y producirá un histograma:hist()

----------Ejemplo 2:
#Un histograma simple:
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
