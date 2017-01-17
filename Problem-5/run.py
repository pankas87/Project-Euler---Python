from functions import *

# Numbers smaller than 10 that are factors of the numbers larger than 10 are removed
  # A number that is divisible by 20 will be divisible by 2 and 4 and 5
  # A number that is divisible by 18 will be divisible by 3 and 6
  # A number that is divisible by 15 will be divisible by 3 and 5
  # With less numbers to divide, the calculations will take less time
numbers = [7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i       = 20

while not is_divisible_by_list(i, numbers):
  # Only multiples of 10 will be divisible by 10, test less numbers and calculate faster
  i += 10
  
  if( i % 10000000 ) == 0:
    print( 'Testing', i )

print('The smallest number divisible by all numbers between 1 and 20 is', str( i ) )
