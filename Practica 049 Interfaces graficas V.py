# Curso Python. Interfaces gráficas V. Vídeo 46
# Widgets Text y Button

from tkinter import*

root= Tk()             

MiFrame=Frame(root, width= 1200, height=900)
MiFrame.pack()

# creamos una variable de nombre para enlazar con la función correspondiente
MiNombre=StringVar()        # StringVar= cadena de caractéres

# cuadros entry
CuadroUsuario=Entry(MiFrame, textvariable=MiNombre) # asociar el entry CuadroUsuario con MiNombre con un segundo  parámetro
CuadroUsuario.grid(row=0, column=1, padx=10, pady=10) 
CuadroUsuario.config(fg="white", bg="black", justify="center")

CuadroContrasena=Entry(MiFrame) 
CuadroContrasena.grid(row=1, column=1, padx=10, pady=10)  
CuadroContrasena.config(fg="white", bg="black", justify="center")
CuadroContrasena.config(show="*") 

CuadroEmail=Entry(MiFrame) 
CuadroEmail.grid(row=2, column=1, padx=10, pady=10)  
CuadroEmail.config(fg="white", bg="black", justify="center")

# cuadro text
TextoComentario=Text(MiFrame, width=50, height=5)      # usamos text para la zona de comentarios / width y height para dimensiones
TextoComentario.grid(row=3, column=1, padx=10, pady=10)  # posicionamos la zona de comentarios
scrollVertical=Scrollbar(MiFrame, command=TextoComentario.yview) # creando el scroll bar
scrollVertical.grid(row=3, column=2, sticky="nsew") # posicionar el scroll bar / sticky para que cubra toda la zona
TextoComentario.config(yscrollcommand=scrollVertical.set) # reparando la barra scroll


# cuadros label
UsuarioLabel=Label(MiFrame, text="Usuario: ")
UsuarioLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

ContrasenaLabel=Label(MiFrame, text="Contraseña: ")
ContrasenaLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10) 

EmailLabel=Label(MiFrame, text="E-mail: ")
EmailLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10) 

ComentarioLabel=Label(MiFrame, text="Comentarios: ")        # añadimos un label de texto
ComentarioLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10) 



# cuadro button
def CodigoBoton():       # definimos una función que reaccione a presionar el botón
    MiNombre.set("Shintesu") 
BotonEnvio=Button(root, text="Enviar", command=CodigoBoton) # crear un botón / command para enlazar con una acción
BotonEnvio.pack()                      # empaquetamos el botón

root.mainloop()