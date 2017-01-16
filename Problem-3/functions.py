def get_largest_prime_factor(n):
  factors = get_prime_factors( n )

  return max( factors )



def get_prime_factors(n):
  divider       = 2
  prime_factors = [ 1 ]

  while n > 1 and divider > 1:
    if ( n % divider ) == 0 and is_prime( divider ):
      prime_factors.append( divider )
      
      n /= divider
      divider = 2
    else:
      divider += 1

  return prime_factors

def is_prime(n):
  # Numbers smaller than or equal to 1 are not prime numbers
  if n <= 1:
    return False

  # Even numbers are not prime numbers
  if ( n > 2 ) and ( n % 2 ) == 0:
    return False
  
  # The largest divisor of any positive number is 
  #  n/2 for even numbers, or a number smaller than n/2 for odd numbers
  top    = int( n / 2 )
  bottom = 3

  while top > bottom:
    if ( n % top ) == 0:
      return False

    if ( n % bottom ) == 0:
      return False

    top    -= 2
    bottom += 2

    

  return True