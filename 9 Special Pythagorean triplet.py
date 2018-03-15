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

for a in range(1, ceil(500 * (2 - sqrt(2)))):
    b = int((1000 * (a - 500)) / (a - 1000))
    c = int(sqrt(a ** 2 + b ** 2))
    if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
        print(a * b * c)
