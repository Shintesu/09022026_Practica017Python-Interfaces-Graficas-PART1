# Curso Python. Interfaces gráficas II. Vídeo 43
# Frames

import os       
from tkinter import *    

raiz=Tk()               
raiz.title("Primera Ventana GUI") 
#raiz.resizable(1,1)     
#raiz.geometry("800x600")       # al añadir un frame no hace falta el geometry (contenedor se adapta al contenido)
raiz.config(bg="violet") 

raiz.config(bd=40) # especificar grosor de borde, de base es 0
raiz.config(relief="sunke")    # configurar borde
raiz.config(cursor="hand2")



icon_path = os.path.join(os.path.dirname(__file__), "WutheringWavesLogo.ico")
raiz.iconbitmap(icon_path)

MiFrame=Frame() # creamos el frame (debe ser empaquetado)
MiFrame.pack(side="bottom", anchor="w") # empaquetamos el frame / side= enlaza una posición / anchor= puntos cardinales
#MiFrame.pack(fill="y", expand="True")    # para rellenar, eje x redimenciona horizontal, para y: (fill="y", expand="True")
#MiFrame.pack(fill="both", expand="True") # para expandir en eje x,y= both
MiFrame.config(bg="cyan")
MiFrame.config(width="650", height="400") # el frame debe tener un tamaño

MiFrame.config(bd=20) # especificar grosor de borde, de base es 0
MiFrame.config(relief="groove")    # configurar borde
MiFrame.config(cursor="pirate")  # configurar cursor


raiz.mainloop()                















