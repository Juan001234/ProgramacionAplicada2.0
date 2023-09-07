a = 1
#value = input('Ingrese un valor: ') #Permite dijitar un valor
#value = int(value)                #convierte ell valor en un entero

while a == 1:                     #Encierra el codigo en un ciclo while
    value = input('Ingrese un valor: ') #Permite dijitar un valor
    value = int(value)                #convierte ell valor en un entero
    for i in range(1,value+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
            
            # print("i = ", i)
            # print("n = ", n)
            # print("residue = ", residue)
            # print("conta = ", conta)
    if conta == 2:
       print(f'{i} es un primo')          #Imprime que es un numero primo si el modulo es 2
       print("\n")
    else:
       print(f'{i} NOOO es un primo')     #Imprime que NO es un numero primo si el modulo es 0
       print("\n")

    print('¿Desea continuar con el programa? Presione 1 para ejecutalo de nuevo:')
    a = input()
    a = int(a)

    if a != 1:
        break

    #value = input('Ingrese un valor') 
    #value = int(value)