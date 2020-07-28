from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
	message1 = "Hola desde el proceso 0"
	comm.send(message1, dest=1, tag=100)
elif rank == 1:
	message2 = comm.recv(source=0, tag=100)
	print(message2)

if rank == 3:
	print("Soy el proceso 3")

# Run: mpiexec -n 2 python hello_mpi.py
# Run: mpiexec -n 3 --use--hwthread-cpus python hello_mpi.py
