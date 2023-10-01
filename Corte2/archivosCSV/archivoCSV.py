import csv
import random
 
# field names
Titulos = ['Nombre', 'Numero_Celular', 'Edad', 'Codigo_Estudiante']
 
# data rows of csv file
Columnas = [ ['Juan Jose', '3165642875', '20', '202120'],
        ['Miguel', '3102314675', '18', '201956'],
        ['Daniel', '3209517538', '25', '202145'],
        ['Estiven', '3174628731', '16', '202045'],
        ['Fernando', '3217412589', '27', '201946'],
        ['Andres', '3143698521', '20', '201945']]
 
# name of csv file
filename = "Datos.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(Titulos)
     
    # writing the data rows
    csvwriter.writerows(Columnas)
