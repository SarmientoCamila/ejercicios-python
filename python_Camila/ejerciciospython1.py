#Hacer un programa que con un botón de consulta muestre el precio de compra y venta del dólar.

import tkinter as tk
from tkinter import messagebox
import requests

def obtener_precio_dolar():
    try:
        # Reemplazar con la URL de la API real para obtener los precios del dólar
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        datos = response.json()
        
        # Valores simulados para compra y venta (puedes adaptarlos según la API)
        precio_compra = datos['rates']['ARS'] * 0.98  # Ejemplo de precio de compra
        precio_venta = datos['rates']['ARS'] * 1.02  # Ejemplo de precio de venta
        
        messagebox.showinfo("Precios del Dólar", 
                            f"Precio de Compra: {precio_compra:.2f} ARS\n"
                            f"Precio de Venta: {precio_venta:.2f} ARS")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener el precio del dólar.\n{e}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Consulta de Precio del Dólar")
ventana.geometry("300x200")

# Botón de consulta
boton_consultar = tk.Button(ventana, text="Consultar Precio del Dólar", command=obtener_precio_dolar)
boton_consultar.pack(pady=50)

# Iniciar la aplicación
ventana.mainloop()
