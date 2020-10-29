'''
def prod(nums): return reduce(lambda x, y: x*y, nums)
# The total factors is the product of 1 more than the power of each prime factor
def count_factors(num):
  prime_powers_plus1 = []
  for p in range(2, num):
    if p * p > num:
      if (num > 1):
        prime_powers_plus1.append(2)
      return numpy.prod(prime_powers_plus1)
    prime_power = 0
    while num % p == 0:
      num /= p
      prime_power += 1
    if prime_power:
      prime_powers_plus1.append(prime_power + 1)
  return 1

n = 1
while True:
  if n % 2 == 1:
    A, B = n, (n+1)/2
  else:
    A, B = n/2, n+1
  numfactors = count_factors(A) * count_factors(B)
  if numfactors > 500:
    print("%s has %s factors" % (A*B, numfactors))
    break
  n += 1
  '''

import functools
def prod(nums): return functools.reduce(lambda x, y: x*y, nums)

# The total factors is the product of 1 more than the power of each prime factor
def count_factors(num):
  prime_powers_plus1 = []
  for p in range(2, num):
    if p * p > num:
      if (num > 1):
        prime_powers_plus1.append(2)
      return prod(prime_powers_plus1)
    prime_power = 0
    while num % p == 0:
      num //= p
      prime_power += 1
    if prime_power:
      prime_powers_plus1.append(prime_power + 1)
  return 1

n = 1
while True:
  if n % 2 == 1:
    A, B = n, (n+1)//2
  else:
    A, B = n//2, n+1
  numfactors = count_factors(A) * count_factors(B)
  # numfactors = count_factors(A * B)
  # print(A*B)
  # if n%10 == 0: print(A*B)
  if numfactors > 500:
    print("%s has %s factors" % (A*B, numfactors))
    break
  n += 1