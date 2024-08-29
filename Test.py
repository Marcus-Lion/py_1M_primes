# to measure exec time
from timeit import default_timer as timer

import numpy as np
from numba import jit, cuda

n = 10000000 * 10

# normal function to run on cpu
def func(a):
    for i in range(n):
        a[i] += 1


# function optimized to run on gpu
@jit()
def func2(a):
    for i in range(n):
        a[i] += 1


if __name__ == "__main__":
    a = np.ones(n, dtype=np.float64)

    start = timer()
    func(a)
    print("without GPU:", timer() - start)

    dev = cuda.get_current_device()
    print("Running on GPU:", dev.name)

    start = timer()
    func2(a)
    print("with GPU:", timer() - start)
