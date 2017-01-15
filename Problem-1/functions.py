def list_natural_multiples_of_3_or_5(start, end):
  multiples = []
  start     = start if start >= 3 else 3
  end       = end if end >= start else start

  for i in range(start, end):
    if ( i % 3 == 0 ) or ( i % 5 == 0 ):
      multiples.append( i )

  return multiples