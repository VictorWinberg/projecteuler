array = range(100 + 1)
sum_of_squares = sum([i ** 2 for i in array])
square_of_sum = sum(array) ** 2

print(square_of_sum - sum_of_squares)