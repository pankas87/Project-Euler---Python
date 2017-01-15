from functions import *
from functools import reduce

natural_multiples_of_3_or_5 = list_natural_multiples_of_3_or_5( 0, 1000 )
sum                         = reduce( lambda x, y: x + y, natural_multiples_of_3_or_5 )

print( 'The sum of the natural numbers from 0 to 1000 that are multiples of 3 or 5 is: ', str( sum ) )
