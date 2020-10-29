
test = sorted('123456789')

def isprime(num): 
    for i in range(2,num):
        if i*i > num:
            return True
        elif num%i == 0:
            return False
for p in range(987654321,1,-2):
    span = str(p)
    if sorted(span) == test[:len(span)]:
        print(p)
        if isprime(p):
            print(p)
            break
'''        

primes = [2]
primesset = set([2])
test = sorted('123456789')
def isprime(num): 
    for p in primes:
        if p*p > num:
            primesset.add(num)
            primes.append(num)
            print(num)
            return True
        elif num%p == 0:
            return False
for num in range(3,987654321,2):
    isprime(num)
for p in reversed(primes):
    span = str(p)
    if sorted(span) == test[:len(span)]:
        print(p)
        break
    '''
