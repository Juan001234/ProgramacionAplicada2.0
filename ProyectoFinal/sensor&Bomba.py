try:
    import usocket as socket
except:
    import socket

import network
from machine import Pin, ADC
import time

ssid = 'Nombre de Red'
password = 'Contraseña'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Conexion correcta')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
led.on()

pin_sensor_humedad = 34

releBomba = 23

# Variable para almacenar el estado actual de la bomba
bomba_activada = False

# Umbral de humedad para encender la bomba (ajusta este valor según tus necesidades)
umbral_encendido = 30


def leer_sensor():
    global hum

    sensor = ADC(Pin(pin_sensor_humedad))
    sensor.atten(ADC.ATTN_11DB)
    valsensor = sensor.read_u16()

    min_original = 65535
    max_original = 30400
    min_destino = 0
    max_destino = 100

    hum = (valsensor - min_original) * (max_destino - min_destino) / (max_original - min_original) + min_destino
    print(hum)
    return hum


def pagina_web():
  html = """<!DOCTYPE HTML>
<html>
<head>
  <meta http-equiv="refresh" content="10">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style>
    html {
     font-family: Arial;
     display: inline-block;
     margin: 0px auto;
     text-align: center;
    }
    h2 { font-size: 3.0rem; }
    p { font-size: 3.0rem; }
    .units { font-size: 1.2rem; }
    .dht-labels{
      font-size: 1.5rem;
      vertical-align:middle;
      padding-bottom: 15px;
    }
  </style>
  <script>
    // Función para realizar una solicitud al servidor al cargar y cada vez que la página se actualiza
    function enviarSolicitud() {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", "/toggle_bomba", true);
      xhr.send();
    }

    // Llamar a la función al cargar la página y configurar un temporizador para que se repita cada 5 segundos
    window.onload = function() {
      enviarSolicitud();
      setInterval(enviarSolicitud, 5000);  // Repetir cada 5 segundos (o ajusta según sea necesario)
    };
  </script>
  </head>
  <body>
    <h2>Datos de sensor</h2>
    <p>
      <i class="fas fa-tint" style="color:#00add6;"></i> 
      <span class="dht-labels">Humedad</span>
      <span>"""+str(hum)+"""</span>
      <sup class="units">%</sup>
    </p>
  </body>
  </html>"""
  return html


def toggle_bomba():
    global bomba_activada
    humedad_actual = leer_sensor()
    rele = Pin(releBomba, Pin.OUT)
    
    # Aquí colocas la lógica para encender o apagar la bomba según el estado actual
    if humedad_actual < umbral_encendido:
        rele.value(1)
        print("Bomba activada")
        # Puedes utilizar un pin específico para controlar la bomba
        # Por ejemplo: Pin(5, Pin.OUT).on()
    else:
        rele.value(0)
        print("Bomba apagada")
        # Puedes utilizar un pin específico para controlar la bomba
        # Por ejemplo: Pin(5, Pin.OUT).off()


def manejar_solicitud(request):
    if 'toggle_bomba' in request:
        toggle_bomba()
        return True
    return False


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conexion, direccion = s.accept()
    print('Nueva conexion desde:  %s' % str(direccion))
    request = conexion.recv(1024)
    print('Solicitud = %s' % str(request))

    if manejar_solicitud(request):
        conexion.send('HTTP/1.1 200 OK\n')
        conexion.send('Content-Type: text/html\n')
        conexion.send('Connection: close\n\n')
        conexion.close()
    else:
        leer_sensor()
        respuesta = pagina_web()
        conexion.send('HTTP/1.1 200 OK\n')
        conexion.send('Content-Type: text/html\n')
        conexion.send('Connection: close\n\n')
        conexion.sendall(respuesta)
        conexion.close()
