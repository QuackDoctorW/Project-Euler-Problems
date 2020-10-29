'''
#basic code

#generate primes as a list(to loop through in order) and set(to test all possible values of f(n))
#limit is set at 2000000, if n equals b, f(n) is divisible by b
#so max of f(n) can be: 1000*2+1000*1000+1000 = 2 million
primes = [2]
primes2 = set()
primes2.add(2)
for num in range(3,2000000,2):
    for p in primes:
        if p*p > num:
            primes.append(num)
            primes2.add(num)
            break
        if num%p == 0:
            break
        if p == primes[-1]:
            primes.append(num)
            primes2.add(num)
            break

#finding a bound for b
#optimize: when n = 0, f(n) is prime if b is prime; max(b) is 1000
#therefore finding all primes under 1000 as possible values of b
primesb= []
for i in primes:
    if i < 1000:
        primesb.append(i)  

#checking for given value of a,b
#optimize: a can only be odd number,otherwise fail 1, since if n is odd then:
#f(n) -> odd*odd + odd*even + odd(since n is prime) -> odd+ even + odd -> even -> cannot be prime
maxcount = [0,0,0] #(a,b,count)
for b in primesb:
    for a in range(-999,1000,2):
        n = 0
        count = 0
        while True:
            number = n*n + n*a + b
            if number in primes2:
                count += 1
                n+=1
            else: 
                break
        if maxcount[2] < count:
            maxcount = [a,b,count]
print(maxcount)
'''
'''
#method2: optimize prime generation time
#this method modifies the above method, to generate prime numbers only if range is needed
primes = [2,3]
primes2 = set()
primes2.add(2)
primes2.add(3)
lasttried = 3
def testprime(primes, lasttried, stop): #only odd numbers are tested, the new start point is last number tried +2 -> always odd, stop is new end of range
  for num in range(lasttried+2,stop,2):
    lasttried = num #update lasttried to the most recently tried
    for p in primes:
      if p*p > num:
        primes.append(num)
        primes2.add(num)
        break
      if num%p == 0:
        break
      if p == primes[-1]:
        primes.append(num)
        primes2.add(num)
        break
        
testprime(primes,lasttried,1000) #instead of 1000, highest b possible is 997, just generating range of b for now
primesb= [] #equals entire list, primesb will be used for range of b, primes will be used to add additional item, primes2 is the growing set
for i in primes:
    primesb.append(i)
print(len(primesb))
    
maxcount = [0,0,0]    
for b in primesb:
  for a in range(-999,1000,2):
    n = 0
    count = 0
    while True:
      number = n*n + n*a + b
      if number > lasttried: #to see if number is out of range of highest primes tested, if so, add additional primes range
        testprime(primes, lasttried, number+1)  #add to primes pool from lasttried to currentnumber    
      if number in primes2: #test if prime
        count += 1
        n+=1
      else: 
        break
    if maxcount[2] < count:
            maxcount = [a,b,count]
print(maxcount)
'''
