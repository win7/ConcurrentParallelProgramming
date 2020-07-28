import threading
from tkinter import *
import random
import time

def worker(numero):
	"""thread worker function"""
	colors = ["red", "green", "blue"]
	x1 = random.randint(0, width)
	y1 = random.randint(0, height)

	color = random.randint(0, len(colors) - 1)

	rectangle = canvas.create_rectangle(x1, y1, x1 + 5, y1 + 5, fill=colors[color])
	print("Hola soy el hilo: " + threading.current_thread().getName())

	for k in range(100):
		# 100, 100
		time.sleep(1)
		movement = random.randint(0, 3)
		if movement == 0:
			x = 0
			y = 5
		elif movement == 1:
			x = 0
			y = -5
		elif movement == 2:
			x = 5
			y = 0
		else:
			x = -5
			y = 0
		canvas.move(rectangle, x, y)
		# 105, 100
	print("Hola soy el hilo: {}. Termine".format(threading.current_thread().getName()))


if __name__ == "__main__":
	width = 600
	height = 600

	master = Tk()

	canvas = Canvas(master, width=width, height=height)
	canvas.pack()
	
	threads = []
	for i in range(100):
		t = threading.Thread(name="HILO {}".format(i) ,target=worker, args=(i,))
		threads.append(t)
		t.start()

	mainloop()
