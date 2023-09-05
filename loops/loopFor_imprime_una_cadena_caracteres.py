import time

cadena = 'TheTimeChamber'

for letra in cadena:
   if letra == 'e': #Omite el caracter e imprime el siguiente
      continue
   print(letra)
   time.sleep(1)
    