# Curso Python. Interfaces gráficas IV. Vídeo 45
# Entry y grid(row, column)

from tkinter import*

root= Tk()              # creamos la raiz

MiFrame=Frame(root, width= 1200, height=900)
MiFrame.pack()

CuadroUsuario=Entry(MiFrame) # creamos el Entry y enlazamos al frame
CuadroUsuario.grid(row=0, column=1, padx=10, pady=10)  # solventar con grid (), funciona como una casilla=tabla
CuadroUsuario.config(fg="white", bg="black", justify="center")

CuadroContrasena=Entry(MiFrame) 
CuadroContrasena.grid(row=1, column=1, padx=10, pady=10)  
CuadroContrasena.config(fg="white", bg="black", justify="center")
CuadroContrasena.config(show="*") # muestra el símbolo seleccionado

CuadroEmail=Entry(MiFrame) 
CuadroEmail.grid(row=2, column=1, padx=10, pady=10)  
CuadroEmail.config(fg="white", bg="black", justify="center")


UsuarioLabel=Label(MiFrame, text="Usuario: ")
#NombreLabel.place(x=80, y=150) # no es la forma adecuada de usar place
UsuarioLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) # grid

ContrasenaLabel=Label(MiFrame, text="Contraseña: ")
ContrasenaLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10) # grid


EmailLabel=Label(MiFrame, text="Dirección E-mail: ")
EmailLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10) # grid

root.mainloop()