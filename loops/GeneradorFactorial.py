while True:

    valor = int(input("Digite un valor entero positivo: "))
    print("Valor: ", valor)
    a = isinstance(valor, int)
    if a == True and valor > 0:
        fact = 1
        for i in range (1, valor + 1):
            fact = fact*i            
        print(f'El factorial de {valor} es: ', fact)
    else:
        print("Porfavor, digite un valor entero positivo")