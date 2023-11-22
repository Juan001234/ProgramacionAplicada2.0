-------------------------------------------------------------------------------------------------------------Matplotlib Adición de líneas de cuadrícula-------------------------------------------------------------------------------------------------------------

____________________Agregar líneas de cuadrícula a un gráfico____________________
#Con Pyplot, puede usar la función para agregar líneas de cuadrícula a la gráfica.grid()

----------Ejemplo 1:
#Agregue líneas de cuadrícula a la gráfica:
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Especificar las líneas de cuadrícula que se van a mostrar____________________
#Puede utilizar el parámetro en la función para especificar qué líneas de cuadrícula para mostrar.axisgrid()

#Los valores legales son: 'x', 'y' y 'ambos'. El valor predeterminado es 'both'.

----------Ejemplo 2:
#Mostrar solo las líneas de cuadrícula para el eje x:
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()

----------Ejemplo 3:
#Mostrar solo las líneas de cuadrícula para el eje Y:
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'y')

plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

____________________Establecer las propiedades de línea de la cuadrícula____________________
#También puede establecer las propiedades de línea de la cuadrícula, de la siguiente manera: grid(color = 'color', linestyle = 'linestyle', linewidth = número).

----------Ejemplo 4:
#Establezca las propiedades de línea de la cuadrícula:
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
