def calc_100m_primes(n: int):
    is_prime = [False, False] + [True] * (n - 1)
    primes = [2]

    for j in range(4, n + 1, 2):
        is_prime[j] = False

    for i in range(3, n + 1, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    print(primes[-10:])
    return len(primes)


print('ml test')
num = calc_100m_primes(200_000_000)
print(f"primes found {num}")
