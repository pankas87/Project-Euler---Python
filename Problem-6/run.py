edge        = 100
sum         = edge * (edge + 1) / 2
sum_squares = (2 * edge + 1) * (edge + 1) * edge / 6

print('sum', sum)
print('sum_squared', sum * sum)
print('sum_squares', sum_squares)
print('sum_squared - sum_squares', sum * sum - sum_squares )