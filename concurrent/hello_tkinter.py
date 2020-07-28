from tkinter import *

ancho = 600
alto = 600

master = Tk()

canvas = Canvas(master, width=ancho, height=alto)
canvas.pack()

canvas.create_rectangle(50, 50, 55, 55, fill="blue")

mainloop()