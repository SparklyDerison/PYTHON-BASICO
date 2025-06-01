from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import sys

#recuerdo de funciones

def cedula():
    pass
    #mostrar que solo pueden ingresar numeros

def peso():
    pass
    #solomante puede ingresar datos no mayor a 200 y numers

def altura():
    pass
    #dar un limite con scroll

def edad(): 
    pass
    #tsolo dar opcciones del uno al cien
def sexo():
    pass
    #2 opciones de sexo
def resultado ():
    pass
    #rtinee que ser una ecuacion sobre los dartos de sexo,edad y peso 

def calorias():
    pass
    #dara las calorias 

def SubidaDePeso():
    pass
    #formula de subida

def BajadaDePeso():  
    pass  
    #formula de bajada

ventana =Tk()#ventana default

#imagenBasal = tk.PhotoImage(file="basal.jpg")
#imagen = tk.Label(ventana,image=imagenBasal)

miframe = Frame(ventana,width=500,height=500)
labelimagen=Label(miframe,text = "bienvenido al registro de taza metabolica basal").place(x=100,y=100)

ventana.title("maricada de jeinner")
ventana.geometry("500x500")

entradaTexto = Entry(ventana) #inicio de preguntas
entradaTexto.pack()

boton = Button(ventana,text = "invoca un saludo")#creacion de boton
boton.place(x=100,y=400)
boton.pack()













#imagen.pack()
miframe.pack()
ventana.mainloop()