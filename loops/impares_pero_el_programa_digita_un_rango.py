# for i in range (1,21):
#     residual = i%2
#     if residual == 0:
#         print(f'{i} is even')
#     else:
#         #print(f'{i} is odd')
#         print(str(i) + ' is odd')

# for i in range (0,6):
#     result = i**3
#     print(result)

times = input("Digite numero de impresiones: ")
times = float(times)
times = int(times)
print(type(times))
print(times)

if times == 0:
    print("Es necesario digitar un numero para continuar con el programa")
else:
    for i in range(1,times+1):
        print("i = ", i)