import numpy as np
from mpi4py import MPI

__all__ = ['map_mpi']


def pmap(func, sequence):
    comm = MPI.COMM_WORLD
    rank = comm.rank
    n_cores = comm.size

    sub_sequence = _get_subsequence_for_my_rank(sequence, rank, n_cores)
    data = func(sub_sequence)

    return comm.gather(data, root=0)

def _get_subsequence_for_my_rank(sequence, rank, n_cores):
    arr = np.array(sequence)
    return np.array_split(arr, n_cores)[rank]
