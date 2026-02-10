# Curso Python. Interfaces gráficas VIII. Vídeo 49
# Función de cálculos

from tkinter import * 

root=Tk() 

MiFrame=Frame(root)
MiFrame.pack()

# operaciones
operacion="" # declaramos una variable con cadena vacía
resultado=0 # almacenar la suma de los valores escritos



# pantalla------------ Debe poder escribir los números presionando el clic 

NumeroPantalla=StringVar()     

pantalla=Entry(MiFrame, textvariable=NumeroPantalla) 
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#2BB110", justify="right")

# Crear una función para poder escribir presionando clics en pantalla-----------------------------------

def NumeroPulsado(num):     

    global operacion                # para que al añadir la suma no se concatene sino que se cree aparte
    if operacion!="":               # condicional "si es diferente de una cadena vacía"
        NumeroPantalla.set(num)     # si es diferente, mostrará el valor del método num por parámetro
        operacion=""                # luego de ejecutar .set(num), operación tiene el valor cadena vacía

    else:                           # si no ha pulsado, continuar con el flujo
        NumeroPantalla.set(NumeroPantalla.get()+num) 

# Definimos una función suma-----------------------------------------------------------------------------
def suma(num):                      # para almacenar debemos añadir un parámetro en la función suma
    global operacion                # se crea una variable global operación
    global resultado                # variable global resultado

    operacion="suma"                # almacenar dentro de la variable global operación el str suma
    resultado+=int(num)             # almacenar dentro de la variable global resultado, siendo un int

    NumeroPantalla.set(resultado)   # para que la calculadora vaya sumando

# Definir función Es_Igual (=)----------------------------------------------------------------------------
def Es_Igual():
    global resultado    # debe operar con la variable global resultado
    
    NumeroPantalla.set(resultado+int(NumeroPantalla.get()))    # refleje en pantalla la suma actual más el último número añadido que no ha sido sumado

    resultado=0         # luego de ejecutar el resultado la variable debe valer 0 para no generar cálculos erróneos


# botones FILA 1 -----------------------------------------------------------------------------------------
Boton7=Button(MiFrame, text="7", width=4, command=lambda:NumeroPulsado("7"))
Boton7.grid(row=2, column=1)
Boton8=Button(MiFrame, text="8", width=4, command=lambda:NumeroPulsado("8"))
Boton8.grid(row=2, column=2)
Boton9=Button(MiFrame, text="9", width=4, command=lambda:NumeroPulsado("9"))
Boton9.grid(row=2, column=3)
BotonDiv=Button(MiFrame, text="/", width=4)
BotonDiv.grid(row=2, column=4)

# botones FILA 2 -----------------------------------------------------------------------------
Boton4=Button(MiFrame, text="4", width=4, command=lambda:NumeroPulsado("4")) 
Boton4.grid(row=3, column=1)
Boton5=Button(MiFrame, text="5", width=4, command=lambda:NumeroPulsado("5"))     
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
BotonSum=Button(MiFrame, text="+", width=4, command=lambda:suma(NumeroPantalla.get())) # parámetro command Lambda que llama a la suma // get para llamar al número en pantalla  
BotonSum.grid(row=5, column=3)
BotonIgual=Button(MiFrame, text="=", width=4, command=lambda:Es_Igual()) # parámetro command Lambda que llama al Es igual (=) al escribirlo
BotonIgual.grid(row=5, column=4)

root.mainloop()