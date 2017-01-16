from functions import *

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,25,30,35,40,45,50,55,60,100,120,180,200,1000,1024,4192,10000,3456789,600851475143]


for number in numbers:
  print( 'Calculating largest prime factor of', str( number )  )

  factor  = get_largest_prime_factor( number )  
  
  print( 'The largest prime factor of', str( number ), 'is', str( factor ) )
