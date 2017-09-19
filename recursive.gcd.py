# a common divisor of two numbers should be able to divise the difference.
def gcd(a, b):
  sma, lar = (a, b) if a<b else (b, a)
  if sma == 0:
    return lar
  return gcd(sma, lar % sma)

def is_power_of_three(n):
  if n % 3 != 0:
    return False
  if n / 3 == 1:
    return True
  return is_power_of_three(n/3)

def is_perfect_square(n):
  def inner(n,k):
    if k * k > n:
      return False
    if k * k == n:
      return True
    return inner(n, k+1)
  return inner(n,1)

print('test is_perfect_square')
print (is_perfect_square(4))
print (is_perfect_square(25))
print (is_perfect_square(8))
print (is_perfect_square(125))
print (is_perfect_square(1))
print (is_perfect_square(0))

print('test is_power_of_three')
print (is_power_of_three(81))
print (is_power_of_three(15))

# test
print (gcd(42, 56)) #14
print (gcd(54, 24)) #6
print (gcd(1, 5)) #1
print (gcd(0, 5)) #5
