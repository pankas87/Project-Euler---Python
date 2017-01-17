def is_divisible_by_list(n, numbers):
  for number in numbers:
    if (n % number) != 0:
      return False

  return True