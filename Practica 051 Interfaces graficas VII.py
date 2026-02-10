# Curso Python. Interfaces gráficas VII. Vídeo 48
# Funcionalidad de una calculadora

from tkinter import * 

root=Tk() 

MiFrame=Frame(root)
MiFrame.pack()

# pantalla------------ Debe poder escribir los números presionando el clic 

NumeroPantalla=StringVar()      # crear una variable y asociarla a la pantalla

pantalla=Entry(MiFrame, textvariable=NumeroPantalla) # 2do parámetro 
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#1cdc3b", justify="right")

# Crear una función para poder escribir presionando clics en pantalla

def NumeroPulsado(num):       # usar Lambda para poder ejecutar la siguiente línea sin generar problemaws, no es lo mejor pero de momento  servirá
    #NumeroPantalla.set(NumeroPantalla.get()+"4")  # para seguir añadiendo un solo número, debemos usar el método get()
    NumeroPantalla.set(NumeroPantalla.get()+num) 


# botones FILA 1 -----------------------------------------------------------------------------
Boton7=Button(MiFrame, text="7", width=4, command=lambda:NumeroPulsado("7"))
Boton7.grid(row=2, column=1)
Boton8=Button(MiFrame, text="8", width=4, command=lambda:NumeroPulsado("8"))
Boton8.grid(row=2, column=2)
Boton9=Button(MiFrame, text="9", width=4, command=lambda:NumeroPulsado("9"))
Boton9.grid(row=2, column=3)
BotonDiv=Button(MiFrame, text="/", width=4)
BotonDiv.grid(row=2, column=4)

# botones FILA 2 -----------------------------------------------------------------------------
Boton4=Button(MiFrame, text="4", width=4, command=lambda:NumeroPulsado("4")) # añadimos un parámetro para llamar a la función / usamos Lambda
Boton4.grid(row=3, column=1)
Boton5=Button(MiFrame, text="5", width=4, command=lambda:NumeroPulsado("5"))                     # pegamos el command lambda en todos los números
Boton5.grid(row=3, column=2)
Boton6=Button(MiFrame, text="6", width=4, command=lambda:NumeroPulsado("6"))
Boton6.grid(row=3, column=3)
BotonMult=Button(MiFrame, text="x", width=4)
BotonMult.grid(row=3, column=4)

# botones FILA 3 -----------------------------------------------------------------------------
Boton1=Button(MiFrame, text="1", width=4, command=lambda:NumeroPulsado("1"))
Boton1.grid(row=4, column=1)
Boton2=Button(MiFrame, text="2", width=4, command=lambda:NumeroPulsado("2"))
Boton2.grid(row=4, column=2)
Boton3=Button(MiFrame, text="3", width=4, command=lambda:NumeroPulsado("3"))
Boton3.grid(row=4, column=3)
BotonRest=Button(MiFrame, text="-", width=4)
BotonRest.grid(row=4, column=4)

# botones FILA 4 -----------------------------------------------------------------------------
Boton0=Button(MiFrame, text="0", width=4, command=lambda:NumeroPulsado("0"))
Boton0.grid(row=5, column=1)
BotonComa=Button(MiFrame, text=".", width=4, command=lambda:NumeroPulsado("."))
BotonComa.grid(row=5, column=2)
BotonSum=Button(MiFrame, text="+", width=4)
BotonSum.grid(row=5, column=3)
BotonIgual=Button(MiFrame, text="=", width=4)
BotonIgual.grid(row=5, column=4)

root.mainloop()