# Problem solutions

### Table of Contents

1. [Multiples of 3 and 5](#001-multiples-of-3-and-5)
2. [Even Fibonacci numbers](#002-even-fibonacci-numbers)
3. [Largest prime factor](#003-largest-prime-factor)
4. [Largest palindrome product](#004-largest-palindrome-product)
5. [Smallest multiple](#005-smallest-multiple)
6. [Sum square difference](#006-sum-square-difference)
7. [10001st prime](#007-10001st-prime)
8. [Largest product in a series](#008-largest-product-in-a-series)
9. [Special Pythagorean triplet](#009-special-pythagorean-triplet)
10. [Summation of primes](#010-summation-of-primes)
11. [Largest product in a grid](#011-largest-product-in-a-grid)
12. [Highly divisible triangular number](#012-highly-divisible-triangular-number)

## Contents

### 001 Multiples of 3 and 5
```python
print(sum([i for i in range(1000) if(i % 3 == 0 or i % 5 == 0)]))

```
Time: `~ 50 ms`.

### 002 Even Fibonacci numbers
```python
def even_fibonacci(a, b, n, total = 0):
    if a > n: return total
    if a % 2 == 0: total += a
    return even_fibonacci(b, a + b, n, total)

print(even_fibonacci(1, 2, 4000000))

```
Time: `~ 50 ms`.

### 003 Largest prime factor
```python
def find_primes(n, i = 1, primes = []):
    if n == 1: return primes

    while n % i != 0: i += 1

    return find_primes(n // i, i + 1, primes + [i])

print(max(find_primes(600851475143)))

```
Time: `~ 50 ms`.

### 004 Largest palindrome product
```python
def isPalindromic(num):
    return num == num[::-1]

palindromes = []
for a in range(100, 1000):
    for b in range(100, 1000):
        product = a * b
        if isPalindromic(str(product)):
            palindromes.append(product)

print(max(palindromes))

```
Time: `~ 700 ms`.

### 005 Smallest multiple
```python
from functools import reduce

def mul(array):
    return reduce(lambda x, y: x * y, array)

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
```
Time: `~ 50 ms`.

### 006 Sum square difference
```python
array = range(100 + 1)
sum_of_squares = sum([i ** 2 for i in array])
square_of_sum = sum(array) ** 2

print(square_of_sum - sum_of_squares)
```
Time: `~ 50 ms`.

### 007 10001st prime
```python
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
```
Time: `~ 400 ms`.

### 008 Largest product in a series
```python
from functools import reduce

def mul(string):
    array = map(int, list(string))
    return reduce(lambda x, y: x * y, array)

def solve(digits):
    return max([mul(digits[i:i + 13]) for i in range(len(digits) + 1 - 13)])

print(solve('7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'))

```
Time: `~ 60 ms`.

### 009 Special Pythagorean triplet
```python
from math import sqrt, ceil

# Given:
#  a ** 2 + b ** 2 = c ** 2,
#  a + b + c = 1000,
#  a < b < c
# Find: a * b * c
# Hence:
#  a < 500 * (2 - sqrt(2)),
#  b = (1000 * (a - 500)) / (a - 1000)
#  c = sqrt(a ** 2 + b ** 2)

n = 1000

for a in range(1, ceil((n / 2) * (2 - sqrt(2)))):
    b = int((n * (a - n / 2)) / (a - n))
    c = int(sqrt(a ** 2 + b ** 2))
    if a + b + c == n and a ** 2 + b ** 2 == c ** 2:
        print(a * b * c)

```
Time: `~ 50 ms`.

### 010 Summation of primes
```python
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
```
Time: `~ 4 s`.

### 011 Largest product in a grid
```python
from functools import reduce

def mul(array):
    if not len(array):
        return 0
    return reduce(lambda x, y: x * y, array)

def solve(M):
    value = 0
    for y, R in enumerate(M):
        for x, C in enumerate(R):
            # Horizontally
            if x + 3 < len(R):
                value = max(value, mul([M[y][x+i] for i in range(4)]))
            # Vertically
            if y + 3 < len(M):
                value = max(value, mul([M[y+i][x] for i in range(4)]))
            # Diagonally
            if x + 3 < len(R) and y + 3 < len(M):
                value = max(value, mul([M[y+i][x+i] for i in range(4)]))
                value = max(value, mul([M[y+3-i][x+i] for i in range(4)]))
    return value


data = [ list(map(int, line.split(' '))) for line in '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''.strip().split('\n') ]

print(solve(data))

```
Time: `~ 60 ms`.

### 012 Highly divisible triangular number
```python
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

```
Time: `~ 1 s`.
