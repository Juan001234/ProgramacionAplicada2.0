import time
inicio = time.time()

for i in range(1,31): #Delimita el rango
    conta = 0
    for n in range(1, i+1): #Obtiene el modulo de los numero
        residue = i%n
        if residue == 0:    #Verifica si el modulo es 0
            conta = conta + 1              
    if conta == 2:
        print(f'{i} es un primo') #En caso de que el modulo sea dos imprime el numero primo
        print("\n")               #Deja espacio entre lineas

fin = time.time()
print("t = ", (fin - inicio)*1000)