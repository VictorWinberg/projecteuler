# Problem solutions

### Table of Contents

1. [001 Multiples of 3 and 5.py](#001-Multiples-of-3-and-5.py)
2. [002 Even Fibonacci numbers.py](#002-Even-Fibonacci-numbers.py)
3. [003 Largest prime factor.py](#003-Largest-prime-factor.py)
4. [004 Largest palindrome product.py](#004-Largest-palindrome-product.py)
5. [005 Smallest multiple.py](#005-Smallest-multiple.py)
6. [006 Sum square difference.py](#006-Sum-square-difference.py)
7. [007 10001st prime.py](#007-10001st-prime.py)
8. [008 Largest product in a series.py](#008-Largest-product-in-a-series.py)
9. [009 Special Pythagorean triplet.py](#009-Special-Pythagorean-triplet.py)
10. [010 Summation of primes.py](#010-Summation-of-primes.py)

## Contents

### 001 Multiples of 3 and 5
```python
print(sum([i for i in range(1000) if(i % 3 == 0 or i % 5 == 0)]))

```
Time: `~ 60 ms`.

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
Time: `~ 800 ms`.

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
Time: `~ 60 ms`.

### 006 Sum square difference
```python
array = range(100 + 1)
sum_of_squares = sum([i ** 2 for i in array])
square_of_sum = sum(array) ** 2

print(square_of_sum - sum_of_squares)
```
Time: `~ 60 ms`.

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

print(solve("7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"))
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
Time: `~ 60 ms`.

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