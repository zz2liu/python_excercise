# a common divisor of two numbers should be able to divise the difference.
def gcd(a, b):
  sma, lar = (a, b) if a<b else (b, a)
  if sma == 0:
    return lar
  return gcd(sma, lar % sma)

# test
print (gcd(42, 56)) #14
print (gcd(54, 24)) #6
print (gcd(1, 5)) #1
print (gcd(0, 5)) #5
