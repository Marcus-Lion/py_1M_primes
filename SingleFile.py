
import subprocess
subprocess.run("python -m pip install numpy", shell=True)

import time
import numpy as np  # 1037 @ 250k

def is_prime(n: int, primes: np.array, lp:int) -> bool:
    a = np.mod(n, primes)
    return (a > 0).sum() == lp

def calc_n_primes(n: int):
    primes = np.array([2], dtype=np.int32)
    i = 3
    lp = len(primes)
    while lp < n:
        if is_prime(i, primes, lp):
            primes = np.append(primes, i)
            lp += 1

            if (lp % 1000) == 0:
                print(f"primes {lp:,} - {100*lp/i:.03f}% - {primes[-3:]}")

        i += 2

    print(primes[-10:])
    return lp

print(f'ml test {__file__}')
tic = time.perf_counter()
num = calc_n_primes(50_000)
toc = time.perf_counter()
print(f"primes found {num} in {toc - tic:.04f}")
