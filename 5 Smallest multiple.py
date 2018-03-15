from functools import reduce

def mul(array):
    return reduce(lambda x, y: x * y, primes)

def missing_prime(i, primes):
    for prime in primes:
        if (prime * mul(primes)) % i == 0:
            return prime

i, n = 1, 20
primes = []
while i < n:
    primes.append(i)
    i += 1
    
    while any([i % prime == 0 for prime in primes if not prime == 1]):
        if not mul(primes) % i == 0:
            primes.append(missing_prime(i, primes))
        i += 1

print(mul(primes))