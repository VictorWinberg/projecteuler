# Sieve of Eratosthenes

i, n = 2, 2000000
primes = [0] * i + list(range(i, n))

while i < n:
    if primes[i] != 0:
        j = i
        while i + j < n:
            primes[i + j] = 0
            j += i
    i += 1

print(sum(primes))