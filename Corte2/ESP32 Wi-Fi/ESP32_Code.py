# Lector Entrada Potenciometro
import time, urequests
import math
from machine import Pin, PWM , ADC

#frecuency = 5000

led = PWM(Pin(2), freq=500, duty=0)


pot = ADC(Pin(34))


#pot.width(ADC.WIDTH_10BIT)


pot.atten(ADC.ATTN_11DB)


url = "https://api.thingspeak.com/update?api_key=RH7O1XR0XNJSPPK0"
#contador = 0


def reconectar():
    print('Fallo de conexion. Reconectando...')
    time.sleep(10)
    reset()
    
while True:
    try:
        pot_value_potenciometro = pot.read()
        
        control_Intensidad = math.trunc(pot_value_potenciometro/4)
        
        led.duty(control_Intensidad)
        
        #time.sleep(0.01)
     
        respuesta = urequests.get(url + "&field1=" +str(control_Intensidad))
        
        print ("Respuesta: " + str(respuesta.status_code))
        respuesta.close ()
    except OSError as e:
        reconectar
