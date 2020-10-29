import math

total = 0
limit = 999999
numlist = [0,1,2,3,4,5,6,7,8,9]
for i in range(9,-1,-1):
    count = 0
    num = math.factorial(i)
    while num <= limit:
        count+=1
        num += math.factorial(i)
    limit -=  math.factorial(i)*count
    total += (10**i)*(numlist[count])
    del numlist[count]

    
    