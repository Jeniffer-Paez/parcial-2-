from tkinter import Tk, Label, Button, Entry, Toplevel, Frame, BOTH, Canvas, BASE, ALTURA, Pendiente 

def graficas():
    print("Grafica")
    BASE = 800
    ALTURA = 800


# ----------------------
# VENTANA PRINCIPAL
# ----------------------
ventana_principal = Tk()
ventana_principal.title("Plano cartesiano")
ventana_principal.resizable(False, False)
ventana_principal.config(bg = "purple")
ventana_principal.geometry("800x800")

# ----------------------
# FRAME GRAFICACIÓN
# ----------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "red", width = 480, height = 400)
frame_graficacion.pack(fill=BOTH, padx = 10, pady = 10)

# ----------------------
# CREACCIÓN CANVA
# ----------------------
C = Canvas(frame_graficacion, width = BASE, height = ALTURA)
C.place(x = 10, y = 10)

# ----------------------
# BOTÓN
# ----------------------
boton = Button(text="Calcular pendiente", padx=10,  fg="white", bg="blue", command= )
boton.pack(side="left", padx=10, pady=10)
graficar = Button(text="Graficar", padx=10,  fg="white", bg="blue", command=graficas)
graficar.pack(side="right", padx=10, pady=10)

# ----------------------
# LINEAS
# ----------------------
linea3 = C.create_line(BASE/2, 0, BASE/2, ALTURA/2, BASE/2, ALTURA, BASE/2, ALTURA/2, fill = "green", width = 5)
linea4 = C.create_line(BASE, ALTURA/2, BASE/2, ALTURA/2, 0, ALTURA/2, BASE/2, ALTURA/2, fill = "pinck", width = 5)

# COORDENADAS
# ----------------------
etiqueta = Label(text="-1, -1", font=("Arial", 20, "bold"))

etiqueta.pack(expand=True)

mostrar_posicion()

ventana_principal.mainloop()
