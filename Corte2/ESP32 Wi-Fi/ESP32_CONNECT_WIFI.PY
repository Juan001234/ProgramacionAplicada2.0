
import network
import machine

# Configuracion de la red Wi-Fi
ssid = "*Nombre de la red*"
password = "*Clave de la red*"

# Crea objeto de red Wi-Fi
wlan = network.WLAN(network.STA_IF)

# Activa el objeto de red Wi-Fi
wlan.active(True)

# Conecta a la red Wi-Fi
wlan.connect(ssid, password)

# Esperar hasta que se establezca la conexión
while not wlan.isconnected():
    pass

# Mostrar la dirección IP
ip_address = wlan.ifconfig()[0]
print("Conectado a la red Wi-Fi. Dirección IP:", ip_address)

# Encender el pin 2
pin = machine.Pin(2, machine.Pin.OUT)
pin.on()
