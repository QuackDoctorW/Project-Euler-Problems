#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
'''
v1
number = 600851475143
currentprime = 2
trylist = list(range(2,number+1))                                                #create a list to try
while number != 1:
    while number%currentprime == 0:                                              #if current prime is a factor, then divide until it's not
        number = number//currentprime
    n = number//currentprime                                                     #to see how many multiples there are in the reduced number, since we don't have to test higher than the reduced number itself i.e 34/2 = 17, when you try until 17, number = 1, while loop breaks
    for i in range(n):                                                           #remove multiples of current prime number
        if (i+1)*currentprime in trylist:                                        #if statement to prevent none error, 6 deleted from list from 2, then 3 again would generate error
            trylist.remove((i+1)*currentprime)
    if trylist != []:
        currentprime  = trylist[0] 
print(currentprime)
v2
#only works for numbers 2 and above
def findbound(minval,maxval):
                for i in range(minval,maxval+1):
                                if maxval%(i) == 0:
                                                while maxval%(i) ==0:
                                                                maxval = maxval//(i)
                                                if maxval == 1:
                                                                return i

                        
                        
number = findbound(2,600851475143)
print(number)
'''
def findbound(minval,maxval):
                for i in range(minval,maxval+1):
                                if maxval%(i) == 0:
                                                while maxval%(i) ==0:
                                                                maxval //= i
                                if maxval**0.5 <=i:
                                                return maxval

                        
                        
number = findbound(2,600851475143)
print(number)

'''
Matt's solution
# an iterable that has 2 3 5 7 9 ...
def potential_primes():
  yield 2
  p = 3
  while True:
    yield p
    p += 2

def factor(num):
  factors = []
  for p in potential_primes():
    if p * p > num:
      factors.append(num)
      return factors
    while num % p == 0:
      num /= p
      factors.append(p)

print(factor(600851475143))
'''