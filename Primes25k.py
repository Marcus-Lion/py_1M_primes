
import time

# import cupy as np  # 34
import numpy as np  # 7.07

from Primes import calc_n_primes

print(f'ml test {__file__}')
np.show_config()
tic = time.perf_counter()
num = calc_n_primes(25_000)
toc = time.perf_counter()
print(f"primes found {num} in {toc - tic:.04f}")
