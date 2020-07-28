from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

list_ = [6, 3, 22, 8, 12, 5, 6, 33, 10, 98, 67, 12, 12, 65, 12, 8, 20, 2, 3, 44]

if rank == 0:
	min_ = min(list_[0:5])

	# recibir al min_ de los demas procesos
	for k in range(1, 4):
		min_1 = comm.recv(source=k, tag=100)
		if min_1 < min_:
			min_ = min_1
	print("El min_ global es: {}".format(min_))

else:
	min_2 = min(list_[5 * rank:5 * rank + 5])
	# 1 -> 5:10
	# 2 -> 10:15
	# 3 -> 15:20
	comm.send(min_2, dest=0, tag=100)

# Run: mpiexec -n 4 --use-hwthread-cpus python min_array.py