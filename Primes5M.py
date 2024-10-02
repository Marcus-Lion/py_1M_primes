import math


def is_prime(n: int, primes: [int]) -> bool:
    # if n < 2: return False

    r = math.sqrt(n)
    for i in primes[1:]:
        if i > r:
            break

        if n % i == 0:
            return False

    return True

def calc_n_primes(n: int):
    print('initializing...')

    primes = [2]

    i = 3
    while len(primes) < n:
        if is_prime(i, primes):
            primes.append(i)
            if (len(primes) % 100) == 0:
                print(f"prime # {len(primes)} found {i}")

        i += 2

    print(primes[-10:])
    return len(primes)


print(f'ml test {__file__}')
num = calc_n_primes(5_000_000)
print(f"primes found {num}")
