import math
def isprime(prime:int) -> bool:
    i = 3
    while i**2 <= prime:
        if prime%i == 0:
            return False
        i += 2
    return True

num = 3
count = 0
while True:
    if isprime(num**2 - (num-1)):
        count+=1
    if isprime(num**2 - (num-1)*2):
        count+=1
    if isprime(num**2 - (num-1)*3):
        count+=1 
    if count/((num)*2-1) < 0.1:        
        break
    num += 2
print(num)
    