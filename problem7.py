import math

i, n = 2, 10001
primes = []

def is_prime(n):
    if n % 2 == 0: return n == 2

    root = int(math.sqrt(n))
    for d in range(3, root + 1):
        if n % d == 0: return False

    return True

while len(primes) < n:
    if is_prime(i):
        primes.append(i)

    i += 1

print(primes[-1])