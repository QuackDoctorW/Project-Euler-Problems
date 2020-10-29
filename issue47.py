primelist = [2,3,5]
primeset = set(primelist)
def isprime(num):
    for  p in primelist:
        if p*p > num:
            primelist.append(num)
            primeset.add(num)
            return True
        elif num%p == 0:
            return False

def getprime(num, count = 1):
    if num ==1:
        return count
    else:
        for p in primelist:
            if num%p == 0:
                t = 1
                value = p**t
                while num%value == 0:
                    t+=1
                    value = p**(t)
                count += getprime(num//(p**(t-1)))
                return count
n = 6
count = 0
while count !=4:
    if not isprime(n):
        count = 0
        for i in [n, n-1,n-2,n-3]:
            if i in primeset:
                break
            if getprime(i) != 5:
                break
            count+=1
    n+=1
print(n-4)
 