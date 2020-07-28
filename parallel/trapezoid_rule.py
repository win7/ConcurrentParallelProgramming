def f(x):
	return x*x + 2

def Trap(a, b, n):
	h = (b - a) / n
	aprox = (f(a) + f(b)) / 2
	for i in range(n - 1):
		x_i = a + i * h
		aprox += f(x_i)
	aprox *= h
	return aprox

if __name__ == "__main__":
	from mpi4py import MPI

	import time

	a = 1
	b = 2
	n = 100000000

	# sequencial version
	""" t_i = time.time()
	

	integral = Trap(a, b, n)
	t_f = time.time()

	runtime = t_f - t_i

	print("Result: {}".format(integral))
	print("Runtime: {}".format(runtime)) """

	# parallel version
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	t_i = time.time()

	h = (b - a) / n

	local_n = int(n / size)
	local_a = a + rank * local_n * h
	local_b = local_a + local_n * h

	local_integral = Trap(local_a, local_b, local_n)

	if rank != 0:
		comm.send(local_integral, dest=0, tag=100)
	else: # proceso = 0
		total_integral = local_integral

		for proc in range(1, size):
			integral_rec = comm.recv(source=proc, tag=100)
			total_integral += integral_rec

	if rank == 0:
		t_f = time.time()
		runtime = t_f - t_i
		print("Result: {}".format(total_integral))
		print("Runtime: {}".format(runtime))

# Run: mpiexec -n 4 --use-hwthread-cpus python trapezoid_rule.py

"""
Secuencial
	n = 100000000
	runtime = 29.3398, 27.2986, 28.0637

Paralelo
n = 100000000
runtime = 17.9250, 19.2626, 21.6766

Speedup = T_secuencial / T_paralela
"""