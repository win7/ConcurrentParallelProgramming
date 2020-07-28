from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(comm)

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
    print("rank {}: {}".format(rank, data))
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print("rank {}: {}".format(rank, data))

if rank == 2:
    data = {'a': 7, 'b': 3.14}
    print("rank {}: {}".format(rank, data))

# Run: mpiexec -n 3 --use-hwthread-cpus python example_mpi.py  