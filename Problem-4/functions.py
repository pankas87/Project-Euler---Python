def is_palindrome(n):
  return n == reverse_number( n )

def reverse_number(n):
  n                  = int( n )
  inverted_positions = []

  while n >= 1:
    inverted_positions.append( n % 10 )

    n = int( n / 10 )

  n                = 0
  decimal_position = 1

  while len( inverted_positions ) > 0:
    n                += inverted_positions.pop() * decimal_position
    decimal_position *= 10

  return n
