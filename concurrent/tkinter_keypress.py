import tkinter as tk
 
root = tk.Tk()
WIDTH = HEIGHT = 400
x1 = y1 = 0


canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
c1 = canvas.create_rectangle(x1, y1, x1 + 5, y1 + 5)
 
left, right, up, down = -5,5,-5,5

global xi
global yi
xi = x1
yi = y1

def keypress(event):
	global text
	global xi
	global yi
	x = 0
	y = 0
	if event.char == "a":
		x = left
		xi += x
	elif event.char == "d":
		x = right
		xi += x
	elif event.char == "w":
		y = up
		yi += y
	elif event.char == "s":
		y = down
		yi += y

	print(x, y, xi, yi)
	canvas.move(c1, x, y)
	 
root.bind("<Key>", keypress)
root.mainloop()