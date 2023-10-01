import csv
import random
 
Titulos = ['Nombre', 'Numero_Celular', 'Edad', 'Codigo_Estudiante']
 # Nombre principal de cada columna

Columnas = [ ['Juan Jose', '3165642875', '20', '202120'],
        ['Miguel', '3102314675', '18', '201956'],
        ['Daniel', '3209517538', '25', '202145'],
        ['Estiven', '3174628731', '16', '202045'],
        ['Fernando', '3217412589', '27', '201946'],
        ['Andres', '3143698521', '20', '201945']]
# Datos de cada columna
 
filename = "Datos.csv"
 # Nobre del archivo CSV

# Escribiendo archivo CSV

with open(filename, 'w') as csvfile:
 
    # Creando archivo CSV
    csvwriter = csv.writer(csvfile)
     
    # Escribiendo titulos de las columnas
    csvwriter.writerow(Titulos)
     
    # Escribiendo datos de las columnas
    csvwriter.writerows(Columnas)
