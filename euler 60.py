from itertools import combinations
from collections import defaultdict
#only test odd numbers
sprimes = {3}
snotprimes = {9}
lprimes = [3]
maxcheck = 3
def getprimes(num):
    global maxcheck
    for n in range(maxcheck+2,num+1,2):
        for p in lprimes:
            if p**2 > n:
                lprimes.append(n)
                sprimes.add(n)
                break
            elif n%p == 0:
                snotprimes.add(n)
                break
    maxcheck = num

def isprime(num):
    if num in sprimes:
        return True
    if num in snotprimes:
        return False
    for i in range(3,num):
        if i**2 > num:
            sprimes.add(num)
            return True
        elif num%i == 0:
            snotprimes.add(num)
            return False

getprimes(10001)
alist = list(lprimes)
deldict = defaultdict(set)


def firsttest(a,indexa):
    for z in alist[indexa+1:-1]:
        first = int(str(a)+str(z))
        second = int(str(z) + str(a))
        if not(isprime(first) and isprime(second)):
            deldict[a].add(z)


def main():
    for indexa in range(len(alist)):
        blist = []
        a = alist[indexa]
        print(a)
        firsttest(a,indexa)
        print(deldict[a])
        for b in alist[indexa+1:-1]:
            if b not in deldict[a]:
                blist.append(b)
        print(len(blist))
        for group in combinations(blist,4):#change to 4 in a bit
            fullgroup = (a,) + (group)
            status = True
            for i,j in combinations(fullgroup,2):
                x  = int(str(i)+str(j))
                y  = int(str(j)+str(i))
                if not (isprime(x) and isprime(y)):
                    deldict[i].add(j)
                    status = False
                    break
            if status:
                return(fullgroup)
    return("no solution")
atuple = main()
print(atuple, sum(atuple))

            

     
            
            
            
        
        
    
        
    
    
    




            
        
    