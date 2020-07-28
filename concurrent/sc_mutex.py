import logging
import random
import threading
import time

class Counter:

	def __init__(self, start=0):
		self.lock = threading.Lock()
		self.value = start

	def increment(self):
		print("Hilo: {} (Waiting for lock)".format(threading.current_thread().getName()))
		self.lock.acquire()
		try:
			print("Hilo: {} (Acquired lock)".format(threading.current_thread().getName()))
			self.value = self.value + 1
		finally:
			self.lock.release()

def worker(c):
	for i in range(2):
		# pause = random.random()
		# print("Sleeping {}".format(pause))
		# time.sleep(pause)
		c.increment()
		print("Hilo: {} ({})".format(threading.current_thread().getName(), c.value))
	print("Hilo: {} (Done)".format(threading.current_thread().getName()))

if __name__ == "__main__":
	counter = Counter()
	for i in range(5):
		t = threading.Thread(target=worker, args=(counter,))
		t.start()

""" 
print("Waiting for worker threads")
main_thread = threading.main_thread()
for t in threading.enumerate():
	if t is not main_thread:
		t.join()
print("Counter: %d", counter.value) 
"""