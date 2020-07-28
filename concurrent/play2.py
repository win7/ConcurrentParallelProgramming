from tkinter import *
import threading
import random as rdn
import time

def worker(numero):
	"""thread worker function"""
	step = 5
	colors = ["red", "green", "blue"]
	x = rdn.randint(1, 500)
	y = rdn.randint(1, 500)

	xi = x
	yi = y

	a1 = canvas.create_rectangle(0, 0, 5, 5, fill=colors[0])
	a2 = canvas.create_rectangle(250, 250, 255, 255, fill=colors[1])
	n3 = canvas.create_rectangle(495, 495, 500, 500, fill=colors[2])

	r = rdn.randint(0, 2)

	img = canvas.create_oval(x, y, x + step, y + step, fill=colors[r])

	""" sign = -1
	for i in range(0, 495, 5):
		sign *= -1
		x = 0
		for j in range(0, 495, 5):
			time.sleep(0.1)
			x = 5 * sign
			xi += x
			canvas.move(img, x, y)
			print("Hola soy el hilo: {} ({},{}) ({},{})".format(threading.current_thread().getName(), xi, yi, x, y))
			y = 0
		y = 5
		yi += y """
			
	while True:
		r = rdn.randint(1, 4)

		if r == 1:
			x = -1 * step
			y = 0
			if xi + x >= 0:
				xi += x
			else:
				x = 0
		elif r == 2:
			x = step
			y = 0
			if xi + x <= width - step:
				xi += x
			else:
				x = 0
		elif r == 3:
			x = 0
			y = -1 * step
			if yi + y >= 0:
				yi += y
			else:
				y = 0
		elif r == 4:
			x = 0
			y = step
			if yi + y <= width - step:
				yi += y
			else:
				y = 0
		
		# print("Hola soy el hilo: {} ({},{})".format(threading.current_thread().getName(), xi, yi))
		canvas.move(img, x, y)

		if xi >= width / 3 and xi <= 2 * (width / 3) - step and yi >= height / 3 and yi <= 2 * (height / 3) - step:
			print("Hola soy el hilo: {}, Finish.".format(threading.current_thread().getName()))
			break
		time.sleep(0.1)

if __name__ == "__main__":
	width = 600
	height = 600

	master = Tk()
	canvas = Canvas(master, width=width, height=height)
	canvas.pack() # this makes it visible

	canvas.create_rectangle(width / 3, height / 3, 2 * (width / 3), 2 * (height / 3), outline="#f11", fill="#1f1", width=2)

	threads = []
	for i in range(500):
		t = threading.Thread(name="HILO {}".format(i) ,target=worker, args=(i,))
		threads.append(t)
		t.start()

	# this creates the loop that makes the window stay 'active'
	mainloop()