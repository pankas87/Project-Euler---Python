from functions import *
from functools import reduce

even_fibonacci_numbers = list_even_fibonacci_numbers( 4000000 )
sum                    = reduce( lambda x, y: x + y, even_fibonacci_numbers )

for even in even_fibonacci_numbers:
  print( str( even ) )

print( 'The sum of the even fibonacci numbers smaller than four million is: ', str( sum ) )