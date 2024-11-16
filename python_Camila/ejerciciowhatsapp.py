
import pywhatkit
from datetime import datetime, timedelta


numero_telefono = "+5491167008959"  
mensaje = "¡Hola! ¿Cómo estás Cami?"


hora_actual = datetime.now()
hora_envio = hora_actual + timedelta(minutes=2)


pywhatkit.sendwhatmsg(
    numero_telefono,
    mensaje,
    hora_envio.hour,  
    hora_envio.minute  
)

#timedelta es una función de la librería datetime que permite calcular la diferencia entre dos fechas o horas.