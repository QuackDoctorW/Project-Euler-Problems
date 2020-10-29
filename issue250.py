import math
def modred(base,exp,thres = 250):
    if base == 0:
        return 0
    if base == 1:
        return 1
    e = math.ceil(math.log(thres,base))
    if e > exp: 
        return (base**exp)
    else: 
        prd = base**(exp%e)
        exp = exp//e 
        base = base**e%thres
        return (modred(base,exp, thres) * prd)%thres 
'''
moddict = {}
for i in range(1,250251):
    r = modred(i,i)
    if r not in moddict:
        moddict[r] = 1
    else:
        moddict[r] +=1
print(moddict)

from itertools import combinations

'''
print(modred(2, 250250,10**16))