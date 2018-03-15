i, n = 2, 10001
primes = []
while len(primes) < n:    
    while any([i % prime == 0 for prime in primes]):
        i += 1

    primes.append(i)
    i += 1

print(primes[-1])