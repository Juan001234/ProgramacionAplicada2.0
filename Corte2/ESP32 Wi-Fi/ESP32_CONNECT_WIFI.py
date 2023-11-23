
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Nobre de la red '
password = 'Contraseña'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Conexión exitosa')
print(station.ifconfig())

#Enciende el del azul del esp32
led = Pin(2, Pin.OUT)
led.on()
