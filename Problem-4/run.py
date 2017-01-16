from functions import *

palindromes = []
start       = 100
stop        = 999
step        = 1

for i in range( start, stop, step ):
  for j in range( start, stop, step ):
    n = i * j

    if is_palindrome( n ):
      palindromes.append( n )

print( 'The largest palindrome product of two 3-digit numbers is', max( palindromes ) )
