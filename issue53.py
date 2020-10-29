import math
count = 0
for i in range(2,101):
    n = i
    limit = n//2
    product = 1
    for r in range(1,limit+1):
        product = product*n/r
        if product > 1000000:
            count += (limit-r+1)*2
            if limit >= r and limit*2==i:
                count-=1
            break
        n -= 1
        r+=1
print(count)
    
        
        
        
        
        
    
    