def even_fibonacci(a, b, n, total = 0):
    if a > n: return total
    if a % 2 == 0: total += a
    return even_fibonacci(b, a + b, n, total)

print(even_fibonacci(1, 2, 4000000))
