from itertools import permutations
from itertools import combinations_with_replacement

def isprime(num):
    for d in range(3,num+1):
        if d*d > num:
            return True
        elif num%d == 0:
            return False
        
def isseq(alist):
    for i in range(len(alist)-2):  
        for j in range(i+1,len(alist)-1):
            for k in range(j+1,len(alist)):
                if alist[k] - alist[j] == alist[j] - alist[i]:
                    return(alist[i],alist[j],alist[k])
    return (0,0,0)  


for c in combinations_with_replacement(range(10),4):
    aset = set()
    for p in permutations(c,):   
        if p[0] != 0 and p[3]%2 != 0:
            num = p[0]*1000 + p[1]*100 + p[2]*10 + p[3]
            if isprime(num):
                aset.add(num)
    if len(aset) > 2:
        if isseq(sorted(aset)) != (0,0,0):
            print(isseq(sorted(aset)))


       
            
            


            

