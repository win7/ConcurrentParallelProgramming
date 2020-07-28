import threading
from tkinter import *
import random as rdn
import time

class Buffer:

	def __init__(self, list_):
		self.lock = threading.Lock()
		self.buffer = list_
		self.total = 0

	def producir(self):
		print("Hilo-P: {} (Waiting for lock)".format(threading.current_thread().getName()))

		x = 0
		y = list_y
		t = rdn.random() / 2
		img = canvas.create_oval(x, y, x + step, y + step, fill="red")
		text = canvas.create_text(x + step / 2, y + step / 2, text=threading.current_thread().getName())

		for k in range(int((list_x - step) / 1)): 
			x = 1
			y = 0
			canvas.move(text, x, y)
			canvas.move(img, x, y)
			time.sleep(t)

		self.lock.acquire()
		if self.total < len(self.buffer):
			try:
				print("Hilo-P: {} (Acquired lock)".format(threading.current_thread().getName()))
				self.total = self.total + 1
				print("Hilo-P: {} (Buffer: {})".format(threading.current_thread().getName(), self.total))

				for k in range(self.total):
					rect = list_[k]
					canvas.itemconfig(rect, fill="red")
			finally:
				self.lock.release()

			canvas.itemconfig(img, fill="white")

			x = 0
			y = -1 * step
		else:
			self.lock.release()
			print("Hilo-P: {} (Not producer)".format(threading.current_thread().getName()))
			x = 0
			y = step

		canvas.move(text, x, y)
		canvas.move(img, x, y)
		for k in range(int((list_x - step) / 1)): 
			time.sleep(t)
			x = -1
			y = 0
			canvas.move(text, x, y)
			canvas.move(img, x, y)
		
	def consumir(self):
		print("Hilo-C: {} (Waiting for lock)".format(threading.current_thread().getName()))

		x = width - step
		y = list_y
		t = rdn.random() / 2
		img = canvas.create_oval(x, y, x + step, y + step, fill="white")
		text = canvas.create_text(x + step / 2, y + step / 2, text=threading.current_thread().getName())

		for k in range(int((list_x - step) / 1)): 
			x = -1
			y = 0
			canvas.move(text, x, y)
			canvas.move(img, x, y)
			time.sleep(t)

		self.lock.acquire()
		if self.total >= 1:
			try:
				print("Hilo-C: {} (Acquired lock)".format(threading.current_thread().getName()))
				self.total = self.total - 1
				print("Hilo-C: {} (Buffer: {})".format(threading.current_thread().getName(), self.total))

				for k in range(len(self.buffer) - 1, self.total - 1, -1):
					rect = list_[k]
					canvas.itemconfig(rect, fill="white")
			finally:
				self.lock.release()

			canvas.itemconfig(img, fill="red")
			x = 0
			y = -1 * step
		else:
			self.lock.release()
			print("Hilo-C: {} (Not consumer)".format(threading.current_thread().getName()))
			x = 0
			y = step

		canvas.move(text, x, y)
		canvas.move(img, x, y)
		for k in range(int((list_x - step) / 1)): 
			time.sleep(t)
			x = 1
			y = 0
			canvas.move(text, x, y)
			canvas.move(img, x, y)

def workerProductor(c):
	for i in range(2):
		pause = rdn.random()
		time.sleep(pause)
		c.producir()
	print("Hilo-P: {} (Done)".format(threading.current_thread().getName()))

def workerConsumidor(c):
	for i in range(2):
		pause = rdn.random()
		time.sleep(pause)
		c.consumir()
	print("Hilo-C: {} (Done)".format(threading.current_thread().getName()))

if __name__ == "__main__":
	width = 600
	height = 300
	step = 30

	buffer_size = 5
	list_ = []
	list_x = (width - buffer_size * step) / 2
	list_y = (height / 2) - (step / 2)

	master = Tk()

	canvas = Canvas(master, width=width, height=height)
	canvas.pack()

	buffer = Buffer(list_)

	for k in range(buffer_size):
		cell = canvas.create_rectangle(list_x + step * k, list_y, list_x + step * k + step, list_y + step,  outline="#000", fill="white", width=2)
		list_.append(cell)

	for i in range(10):
		p = threading.Thread(name="{}".format(i), target=workerProductor, args=(buffer,))
		p.start()

	for i in range(15):
		c = threading.Thread(name="{}".format(i), target=workerConsumidor, args=(buffer,))
		c.start()

	mainloop()

""" 
print("Waiting for worker threads")
main_thread = threading.main_thread()
for t in threading.enumerate():
	if t is not main_thread:
		t.join()
print("Buffer: %d", counter.total) 
"""
