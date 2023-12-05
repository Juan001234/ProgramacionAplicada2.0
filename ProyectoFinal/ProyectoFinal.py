try:
    import usocket as socket
except:
    import socket

import network
from machine import Pin, ADC
import time
import ntptime
import utime

ssid = 'Nombre de Red'
password = 'Clave'

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
releBomba = 21
releBombillo = 22 # Ajusta el pin del bombillo

# Variable para almacenar el estado actual de la bomba
bomba_activada = False

# Umbral de humedad para encender la bomba (ajusta este valor según tus necesidades)
umbral_encendido = 30

# Define el horario para encender y apagar el bombillo (ejemplo: de 18:30 a 3:30 del día siguiente)
hora_encendido = 18
minutos_encendido = 30
hora_apagado = 23
minutos_apagado = 30

def leer_sensor():
    global hum

    sensor = ADC(Pin(pin_sensor_humedad))
    sensor.atten(ADC.ATTN_11DB)
    valsensor = sensor.read()

    min_original = 4095
    max_original = 2890
    min_destino = 0
    max_destino = 100

    hum = (valsensor - min_original) * (max_destino - min_destino) / (max_original - min_original) + min_destino
    print(hum)
    return hum

def obtener_fechahora():
    try:
        ntptime.settime()
    except OSError as e:
        print("Error al obtener la hora desde NTP:", e)
        # Puedes manejar el error de otra manera, como intentar nuevamente o usar una hora predeterminada.
        return None
    
    try:
        # Obtiene la fecha y hora actual en tiempo UTC
        rtc_time_utc = utime.localtime()
        
        # Convierte el tiempo UTC a tiempo local (Bogotá, Colombia - UTC-5)
        rtc_time_bogota = utime.localtime(utime.mktime(rtc_time_utc) - 5 * 3600)
    
        print("Fecha y hora actual en Bogotá, Colombia:", rtc_time_bogota)
        return rtc_time_bogota
    except (OverflowError, ValueError) as e:
        print("Error al convertir tiempo:", e)
        return None

def pagina_web():
    # Obtener la fecha y hora
    fecha_hora = obtener_fechahora()

    if fecha_hora is not None:
        hum = leer_sensor()
        
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
    // Función para realizar solicitudes al servidor al cargar y cada vez que la página se actualiza
    function enviarSolicitudes() {
        var xhrBomba = new XMLHttpRequest();
        xhrBomba.open("GET", "/toggle_bomba", true);
        xhrBomba.send();

        var xhrBombillo = new XMLHttpRequest();
        xhrBombillo.open("GET", "/toggle_bombillo", true);
        xhrBombillo.send();
    }

    // Llamar a la función al cargar la página y configurar un temporizador para que se repita cada 5 segundos
    window.onload = function() {
        enviarSolicitudes();
        //setInterval(enviarSolicitudes, 10000);  // Repetir cada 5 segundos (o ajusta según sea necesario)
    };
</script>
        </head>
        <body>
          <h2>Datos de sensor</h2>
          <p>
            <i class="fas fa-tint" style="color:#00add6;"></i> 
            <span class="dht-labels">Humedad</span>
            <span>"""+str(hum)+"""%</span>
          </p>
          <h2>Hora del Dia</h2>
          <p>
            <i class="fas fa-tint" style="color:#00add6;"></i> 
            <span>"""+str(fecha_hora[3])+""":"""+str(fecha_hora[4])+"""</span>
          </p>
        </body>
        </html>"""

        return html
    else:
        # Handle the case where fecha_hora is None
        return "Error al obtener la fecha y hora."


def toggle_bombillo():
    global bombillo_encendido
    bombillo = Pin(releBombillo, Pin.OUT)

    # Obtiene y muestra la hora local en formato de 24 horas
    fecha_hora = obtener_fechahora()

    if fecha_hora is not None:
        rtc_time_bogota = fecha_hora
        hora_local = fecha_hora[3]
        minutos_local = fecha_hora[4]
        
        # Verifica si es el momento de encender o apagar el bombillo
        if (hora_local > hora_apagado) or \
           (hora_local == hora_apagado and minutos_local >= minutos_apagado):
            # Apaga el bombillo
            bombillo.off()
            print("Bombillo apagado")
            print("Hora local:", hora_local)
            print("Minutos local:", minutos_local)
        else:

            if (hora_local > hora_encendido) or \
               (hora_local == hora_encendido and minutos_local >= minutos_encendido):
                # Enciende el bombillo
                bombillo.on()
                print("Bombillo encendido")
                print("Hora local:", hora_local)
                print("Minutos local:", minutos_local)
            else:
                # Apaga el bombillo
                bombillo.off()
                print("Bombillo apagado")
                print("Hora local:", hora_local)
                print("Minutos local:", minutos_local)
    else:
        print("Error al obtener la fecha y hora. Bombillo no modificado.")

def toggle_bomba():
    global bomba_activada
    humedad_actual = leer_sensor()
    rele = Pin(releBomba, Pin.OUT)
    
    # Aquí colocas la lógica para encender o apagar la bomba según el estado actual
    if humedad_actual < umbral_encendido:
        rele.value(0)
        print("Enviando un chorro de agua a la planta")
        time.sleep(2.5)
        rele.value(1)
        time.sleep(2.5)
        # Puedes utilizar un pin específico para controlar la bomba
        # Por ejemplo: Pin(5, Pin.OUT).on()
    else:
        rele.value(1)
        print("Bomba apagada")
        # Puedes utilizar un pin específico para controlar la bomba
        # Por ejemplo: Pin(5, Pin.OUT).off()

# ...

def manejar_solicitud(request):
    if 'toggle_bomba' in request:
        toggle_bomba()
        return True
    if 'toggle_bombillo' in request:
        toggle_bombillo()
        return True
    return False

#def manejar_solicitud(request):
    #if 'toggle_bombillo' in request:
        #toggle_bomba()
        #return True
    #return False

# Configuración del servidor web
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

 
