def list_even_fibonacci_numbers(n):
  even = []
  a, b = 0, 1
  n    = n if n >= 1 else 1

  while a < n:
    if ( a % 2 == 0 ):
      even.append( a )
    
    a, b = b, a + b

  return even