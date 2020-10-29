

'''
def calc(y):
     return y**2+1/D+2/D*((1+D*y**2)**0.5)
D = 6
y = 3/D
count = 2
while y%1 != 0:
     y = calc(y)
     count +=1
print(count)
'''
'''
num = 0
for D in range(1,61): 
    if (D**0.5)%1 != 0:
        count = 2
        while (((count**2-1)/D)**0.5)%1 != 0:
            count += 1
            
        if num< count: 
            num = count
        print(D, count, (((count**2-1)/D)**0.5))


#generate a list or primes under 1000:
import math
plist = [2]
for num in range(3,1000):
    for p in plist:
        if num%p == 0:
            break
        if p > math.sqrt(num): #can technically do it until sqrt 
            plist.append(num)
print(plist)
'''



    
    
    

            
