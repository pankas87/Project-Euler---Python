sum         = 0
sum_squares = 0
sum_squared = 0

for val in range(1,101):
  sum         += val
  sum_squares += val * val

sum_squared = sum * sum

print('sum', sum)
print('sum_squared', sum_squared)
print('sum_squares', sum_squares)
print('sum_squared - sum_squares', sum_squared - sum_squares )