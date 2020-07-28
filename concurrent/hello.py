import threading

def worker(numero):
    """thread worker function"""
    print("Hola soy el hilo: " + threading.current_thread().getName())

hilos = []
for i in range(10):
    t = threading.Thread(name="HILO {}".format(i) ,target=worker, args=(i,))
    hilos.append(t)
    t.start()

# print(hilos)
# Tupla Lista