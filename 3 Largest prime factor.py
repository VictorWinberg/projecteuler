def find_primes(n, i = 1, primes = []):
    if n == 1: return primes

    while n % i != 0: i += 1

    return find_primes(n // i, i + 1, primes + [i])

print(max(find_primes(600851475143)))
