from itertools import count, tee, groupby
from functools import reduce

def gen_primes():
    '''Sieve of Eratosthenes with yield'''
    # a composite number is a non-prime number
    composite = {}
    for i in count(2):
        number = composite.pop(i, None)
        # if number is not composite => number is prime
        if number is None:
            yield i
            composite[i*i] = i
        else:
            x = number + i
            while x in composite: x += number
            # add next composite number
            composite[x] = number

def gen_tris():
    for i in count(1): yield i * ( i + 1) // 2

def get_factors(divisors):
    factors = [len(list(group)) for _, group in groupby(divisors)]
    return reduce(lambda a, b: a * (b + 1), [1] + factors)

prime_gen = gen_primes()

for tri in gen_tris():
    x = tri
    divisors = []
    primes, prime_gen = tee(prime_gen)
    for prime in primes:
        if prime > x: break
        while x % prime == 0:
            x //= prime
            divisors.append(prime)
    if get_factors(divisors) > 500: break

print(tri)
