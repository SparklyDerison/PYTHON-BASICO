from  tkinter import *
ventana =Tk()#ventana default

imagenBasal=PhotoImage(file = "/home/sparkly/Imágenes/basal.jpg")

miframe = Frame(ventana,width=500,height=500)
label=Label(miframe,text = "bienvenido al registro de taza metabolica basal").place(x=100,y=100)

ventana.title("maricada de jeinner")
ventana.geometry("500x500")

entradaTexto = Entry(ventana) #inicio de preguntas
entradaTexto.pack()

boton = Button(ventana,text = "invoca un saludo")#creacion de boton
boton.place(x=100,y=400)
boton.pack()

miframe.pack()
ventana.mainloop()