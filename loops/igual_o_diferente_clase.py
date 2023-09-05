a = input("Digite numero 'a': ")
a = int(a)
b = input("Digite numero 'b': ")
b = float(b)
c = a + b

if a == b:
    print("iguales")
else:
    print("diferentes")

print("La clase de a es: ", type(a))
print("la clase de b es: ", type(b))
print("La suma de 'a' y 'b' es = ", c)

if type(a) == type(b):
    print("a y b son del la misma clase")
else:
    print("a y b son de diferente clase")