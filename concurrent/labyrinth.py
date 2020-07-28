from tkinter import *
import threading
import random as rdn
import time

# reference: https://ic1800astep11.wordpress.com/step13/11/11/030-backtracking-el-problema-del-laberinto/
""" Crea un laberinto a partir de una tira de entrada.
    Entradas:
         stringLab : tira que contiene el diseño del
                     laberinto.
    Salidas:
         Laberinto representado por una matriz, tal que
         la entrada i,j contiene: 
         0 - si la casilla está libre
         1 - si hay pared
         2 - posición en donde está el queso.
    Restricciones:
         Todas las entradas de la tira son 0, 1 o 3. Las
         filas se representan por un cambio de línea.
         No hay líneas vacías.
"""


laberinto = [
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,1],
    [1,0,1,0,1,1,0,1,0,1,1],
    [1,0,1,0,0,0,0,1,0,1,1],
    [1,1,1,0,1,1,0,1,0,0,1],
    [1,0,0,0,1,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,3,1,1,0,0,1,0,1],
    [1,0,1,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1]
]

def impLab(laberinto):         
    for i, x in enumerate(laberinto):
        for j, y in enumerate(x):
            if y == 1:
                canvas.create_rectangle(j*step, i*step, j*step+step, i*step+step, outline="#f11", fill="#1f1")
 

def recorrido(i, j):
    """ Dado un laberinto en donde se ubica un queso,
        retorna en una lista de pares ordenados (x,y)
        que indican el camino desde una posición inicial
        (i,j) hasta la posición en que se encuentra el
        queso.
        Entradas:
             (i, j) : posición inicial a partir de donde
                      se realizará la búsqueda de un camino
                      hasta la posición del queso.
        Salidas:
             Lista con las casillas, expresadas como pares
             ordenados, que llevan desde la posición inicial
             hasta la posición en que se encuentra el queso.
             Si no existe un camino retorna la lista vacía.
    """
    
    if laberinto[i][j] == 3:
        return [(i, j)]
 
    if laberinto[i][j] == 1:
        return []
 
    laberinto[i][j] = -1
 
    if i > 0 and laberinto[i - 1][j] in [0, 3]:                     # Norte
        camino = recorrido(i - 1, j)
        if camino:
            return [(i, j)] + camino
 
    if j < len(laberinto[i]) - 1 and laberinto[i][j + 1] in [0, 3]: # Este
        camino = recorrido(i, j + 1)
        if camino:
            return [(i, j)] + camino
 
    if i < len(laberinto) - 1 and laberinto[i + 1][j] in [0, 3]:    # Sur
        camino = recorrido(i + 1, j)
        if camino:
            return [(i, j)] + camino
 
    if j > 0 and laberinto[i][j - 1] in [0, 3]:                     # Oeste
        camino = recorrido(i, j - 1) 
        if camino:
            return [(i, j)] + camino
 
    return []
 
def worker(numero):
    """thread worker function"""
    colors = ["red", "green", "blue"]
    x = 1 # rdn.randint(1, 500)
    y = 1 #rdn.randint(1, 500)

    xi = x
    yi = y

    r = rdn.randint(0, 2)
    img = canvas.create_oval(x*step, y*step, x*step + step, y*step + step, fill=colors[r])
    
    for item in okok: 
        x = (item[0] - xi) * step
        y = (item[1] - yi) * step
        xi = item[0]
        yi = item[1]

        canvas.move(img, y, x)
        time.sleep(rdn.randint(0, 10) / 10)
        print("Hola soy el hilo: {} ({},{})".format(threading.current_thread().getName(), x, y))
    

if __name__ == "__main__":
    step = 30
    width = len(laberinto[0]) * step
    height = len(laberinto) * step

    master = Tk()
    canvas = Canvas(master, width=width, height=height)
    canvas.pack() # this makes it visible

    # canvas.create_rectangle(width / 3, height / 3, 2 * (width / 3), 2 * (height / 3), outline="#f11", fill="#1f1", width=2)

    # laberinto = creaLaberinto(stringLab)
    # print(laberinto)
    impLab(laberinto)
    okok = recorrido(1, 1)
    hilos = []
    for i in range(10):
        t = threading.Thread(name="HILO {}".format(i) ,target=worker, args=(i,))
        hilos.append(t)
        t.start()

    # this creates the loop that makes the window stay "active"
    mainloop()