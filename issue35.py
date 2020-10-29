#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

primelist = [2]        
def isprime(num: int) -> bool:
    for p in primelist:
        if p*p > num:     
            primelist.append(num)
            return True
        if num%p == 0:
            return False

for i in range(3,1000001,2):
    isprime(i)
    
primeset = set(primelist) 
def isrot(prime: int) -> bool:
    sprime = str(prime)
    if len(sprime) == 1:
        return True
    for i in range(1,len(sprime)):
        snew = sprime[i:]+sprime[:i]
        if int(snew) not in primeset:
            return False
    return True   

count = 0
for j in primelist:
    if isrot(j):
        count+=1
print(count)
    
            