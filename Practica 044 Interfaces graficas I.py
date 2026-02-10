# Curso Python. Interfaces gráficas I. Vídeo 42
import os           # importamos os para solucionar el error del icono
from tkinter import *     # importar de tkinter todas las clases

raiz=Tk()                 # creamos una raíz y llamamos a la clase

raiz.title("Primera Ventana GUI") # creamos el título 

raiz.resizable(1,1)       # para redimensionar la ventana (width y height)

# Ruta absoluta al ícono (ya que generó error en la forma del video)
icon_path = os.path.join(os.path.dirname(__file__), "WutheringWavesLogo.ico")
raiz.iconbitmap(icon_path)

raiz.geometry("800x600")       # tamaño por defecto

raiz.config(bg="violet")

raiz.mainloop()                # usamos el método mainloop() para mantener abierta la ventana















