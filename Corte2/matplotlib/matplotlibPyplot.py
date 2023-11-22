-------------------------------------------------------------------------------------------------------------Matplotlib Pyplot-------------------------------------------------------------------------------------------------------------

____________________Pyplot____________________
#La mayoría de las utilidades de Matplotlib se encuentran bajo el submódulo, y se importan normalmente bajo el alias:pyplotplt
import matplotlib.pyplot as plt
#Ahora se puede hacer referencia al paquete Pyplot como .plt

----------Ejemplo 1:
#Dibuje una línea en un diagrama desde la posición (0,0) hasta la posición (6.250):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
