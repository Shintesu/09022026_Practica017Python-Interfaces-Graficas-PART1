# Curso Python. Interfaces gráficas III. Vídeo 44
# librería tkinter. Widget Label

from tkinter import *
import os

# variableLabel=Label(Contenedor, Opciones)    # sixtaxis

root=Tk()        # creamos la raíz

MiFrame=Frame(root, width=600, height=600) # creamos un frame, usamos la clase/// constructor enlazado a root
MiFrame.pack() # lo empacatamos

# ruta absoluta porque genera error xd
ruta_imagen =os.path.join(os.path.dirname(__file__), "popcat.gif")
MiImagen=PhotoImage(file=ruta_imagen)   # ubicamos la variable ruta
Label(MiFrame, image=MiImagen).place(x=50, y=50) # label de imagen



#MiLabel=Label(MiFrame, text="Bienvenidos, a los juegos del hambre")  # usando Label, text
#MiLabel.place(x=100, y=200)        # no empaquetamos, usaremos place (x= , y= )

# comentamos el label de texto para dar espacio al de imagen:
MiTexto1=Label(MiFrame, text="Bienvenidos, a los juegos del hambre", fg="Blue", font=("Comic Sans MS", 18)).place(x=85, y=70)
#MiTexto1.place(x=85, y=70)

MiTexto2=Label(MiFrame, text="POP POP POP!", fg="Blue", font=("Comic Sans MS", 25)).place(x=175, y=485)
#MiTexto2.place(x=175, y=485)

root.mainloop() # bucle infinito      
















