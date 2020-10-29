import math
def modred(base,exp,thres = 10000000000):
    if base == 0:
        return 0
    if base == 1:
        return 1
    e = math.ceil(math.log(thres,base))
    if e > exp: 
        return base**exp
    else: 
        prd = base**(exp%e)
        exp = exp//e 
        base = base**e%thres
        return (modred(base,exp) * prd)%thres 


total = 0
for i in range(1,101):
    total += modred(i,i)
print(total%10000000000)


                
                
            
