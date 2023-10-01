import random

numerosAleatorios = [random.random() for x in range(0,10)]

with open("numerosAleatorios.txt", "w") as file:
    for number in numerosAleatorios:
        file.write(str(number) + "\n")
