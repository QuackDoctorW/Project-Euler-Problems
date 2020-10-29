adict = {}
amax = [1,1]
limit = 1000000
#optimization
#only do odd number under limit, since a even number  always divide by 2 a number of times -> every even number has an odd reduced representation; 8 -> 1, 20 -> 5
#so I am calculating for longest chainthat begins with odd number; mult2 function is used to calculate up to real
# value; if 499,999 gave me the longest chain stat w an odd, then 999,998 would be the longest chain; no number is missed. 999999 would be tested. 
#every time a new number count is calculated, so numbers do not need to be calcuted again
#collatz func-> if odd, check dictionary, if not add to dict;
#instead of making 2 step for 3n+1 and then /2, combined into one step
def collatz(num, adict, count=1):
    if num == 1:
        return count       
    elif num%2 == 1:
        if num in adict:
            return adict[num]
        else:
            count = 2 + collatz((3*num+1)/2, adict, count)
            adict[num] = count           
            return count
    elif num%2 == 0:
        if num in adict:
            return adict[num]     
        else:
            count = 1+ collatz(num/2, adict, count)
            return count
'''       
def mult2(num, alimit=limit):
    count = -1
    while num <= alimit:
        count+=1
        num = 2*num
    return count

for i in range(int(limit/2)):
    number = collatz(2*i+1,adict)+mult2(2*i+1)
    if number > amax[1]:
        amax = [(2*i+1)*(2**mult2(2*i+1)), number]
'''
for i in range(50000,1000001):
    number = collatz(i,adict) 
    if number > amax[1]:
        amax = (i, number)
print(amax)
        
    

