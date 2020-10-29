high = 0

def collatz(num, count=1) -> int:
    if num%2 == 0:
        count = collatz(num/2, count= count+1)
    elif num != 1:
        count = collatz(3*num+1, count =  count+1)
    return count
for i in range(1,1000001):
    high = max(high, collatz(i))
print()    
        


