#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
'''
#this one is too slow
maximum = 1000
primesum = 2
trylist = list(range(maximum+1))[3::2]
def reduceby(prime,alist):
    for i in alist:
        if i%prime==0:
            alist.remove(i)
while trylist != []:
    currentprime = trylist[0] 
    primesum += currentprime
    reduceby(currentprime,trylist)
print(primesum)

#this one is too slow too
maximum = 2000000
primesum = 2
trylist = list(range(maximum+1))[3::2]
def reduceby(prime,alist):
    count = 0
    for i in range(len(alist)):
        if alist[i-count]%prime==0:
            alist.remove(alist[i-count])
            count +=1
while trylist != []:
    currentprime = trylist[0] 
    primesum += currentprime
    reduceby(currentprime,trylist)
print(primesum)
#


'''
maximum = 2000000
prime = [2]
primesum = 2
for n in range(3,maximum+1,2):
 for p in prime:
  if p**2 > n:
   prime.append(n)
   primesum += n
   break
  if n%p == 0:
   break
  elif p == prime[-1]:
   prime.append(n)
   primesum += n
print(primesum)

