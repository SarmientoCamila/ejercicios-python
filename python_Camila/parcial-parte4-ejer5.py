# Escribe un programa que muestre la fecha y hora actuales y permita agregarle 10 días.

from datetime import datetime, timedelta

fecha_actual = datetime.now()
print(f"Fecha y hora actuales: {fecha_actual}")


nuevafecha = fecha_actual + timedelta(days=10)
print(f"Fecha y hora después de agregar 10 días: {nuevafecha}")

