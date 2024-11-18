import time

import numpy as np

from Primes import calc_n_primes

print(f'ml test {__file__}')
np.show_config()

tic = time.perf_counter()
num = calc_n_primes(5_000_000)
toc = time.perf_counter()
print(f"primes found {num} in {toc - tic:.04f}")
