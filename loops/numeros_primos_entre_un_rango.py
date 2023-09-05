import time
inicio = time.time()

for i in range(0,31):  #Delimita el rango
    conta = 0
    for n in range(1, i+1): #analiza los numeros primos entre 1 y i+1
        residue = i%n
        if residue == 0:      #verifica el modulo para saber si es un numero primo
            conta = conta + 1  
              
    if conta == 2:
        print(f'{i} es un primo') #imprime el numero primo
        
fin = time.time()
print("t = ", (fin - inicio)*1000)