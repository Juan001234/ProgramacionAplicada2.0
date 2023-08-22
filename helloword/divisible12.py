# En un rango de 100 hasta 301, imprime todos los numeros
#  cuyo modulo de 12 es 0
for i in range(100, 301):
    if (i%12) != 0:
        continue
    print(i) 