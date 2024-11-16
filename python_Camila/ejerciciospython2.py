##calculadora basica

import tkinter as tk


def click_boton(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, actual + str(valor))

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
        
ventana = tk.Tk()
ventana.geometry("350x250")
ventana.title("Calculadora")

entrada = tk.Entry(ventana, font=("Arial", 18), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4, pady=10)

# Botones con las funciones asignadas
tk.Button(ventana, text="1", width=10, height=2, command=lambda: click_boton(1)).grid(row=1, column=0)
tk.Button(ventana, text="2", width=10, height=2, command=lambda: click_boton(2)).grid(row=1, column=1)
tk.Button(ventana, text="3", width=10, height=2, command=lambda: click_boton(3)).grid(row=1, column=2)
tk.Button(ventana, text="+", width=10, height=2, command=lambda: click_boton("+")).grid(row=1, column=3)
tk.Button(ventana, text="4", width=10, height=2, command=lambda: click_boton(4)).grid(row=2, column=0)
tk.Button(ventana, text="5", width=10, height=2, command=lambda: click_boton(5)).grid(row=2, column=1)
tk.Button(ventana, text="6", width=10, height=2, command=lambda: click_boton(6)).grid(row=2, column=2)
tk.Button(ventana, text="-", width=10, height=2, command=lambda: click_boton("-")).grid(row=2, column=3)
tk.Button(ventana, text="7", width=10, height=2, command=lambda: click_boton(7)).grid(row=3, column=0)
tk.Button(ventana, text="8", width=10, height=2, command=lambda: click_boton(8)).grid(row=3, column=1)
tk.Button(ventana, text="9", width=10, height=2, command=lambda: click_boton(9)).grid(row=3, column=2)
tk.Button(ventana, text="*", width=10, height=2, command=lambda: click_boton("*")).grid(row=3, column=3)
tk.Button(ventana, text="0", width=10, height=2, command=lambda: click_boton(0)).grid(row=4, column=0)
tk.Button(ventana, text="Clear", width=10, height=2, command=limpiar).grid(row=4, column=1)
tk.Button(ventana, text="=", width=10, height=2, command=calcular).grid(row=4, column=2)
tk.Button(ventana, text="/", width=10, height=2, command=lambda: click_boton("/")).grid(row=4, column=3)

ventana.mainloop()