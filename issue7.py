#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?
def numgen():
    n = 1
    while True:
        n += 2        
        yield n
        
def isprime(n):
    for p in primes:
        if n%p == 0:
            return False
        elif p == primes[-1]:
            return True
            
        
def countprime():
    count = 1
    while count < threshold:
        n = next(numbers)
        if isprime(n)==True:
            count+=1
            primes.append(n)
    print(n)
   
numbers = numgen()             
primes = [2]
threshold = 10001
countprime()







            
