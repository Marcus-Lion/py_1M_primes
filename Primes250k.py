import time

import cupy as np  # 574s

from Primes import calc_n_primes

# import numpy as np  # 1037

print(f'ml test {__file__}')
np.show_config()
tic = time.perf_counter()
num = calc_n_primes(250_000)
toc = time.perf_counter()
print(f"primes found {num} in {toc - tic:.04f}")
