def isPalindromic(num):
    return num == num[::-1]

palindromes = []
for a in range(100, 1000):
    for b in range(100, 1000):
        product = a * b
        if isPalindromic(str(product)):
            palindromes.append(product)

print(max(palindromes))
