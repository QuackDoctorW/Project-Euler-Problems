

'''
#too slow
testlist = sorted('123456789')
testset = set(testlist)
aset = set()

for i in range(1,987):
    diffset = testset - set(sorted(str(i)))
    start = ''
    finish = ''
    for i in sorted(diffset):
        start += i
        finish = i + finish
    for j in range(int(start),int(finish)):
        if sorted(str(i*j)+str(i)+str(j)) == testlist:
            if i*j not in aset:
                aset.add(i*j) 
print(len(aset))
'''

testlist = sorted('123456789')
count = 0

for product in range (1234,9877):  #only a four digit number can be created using 1-9 exactly once
    for i in range(1,100):         #to obtain a four digit number, can onely be 3dig x 2 dig or 4dig x 1dig, going through all the number up to two digits
        if product%i == 0:         #if divides evenly
            j = product//i         #get the other divisor
            if sorted(str(product)+str(i)+str(j)) == testlist: #see if all three uses 1-9 exactly once, if so add, no isses of repeating since a set is used
                count += product
                break
print(count)


#method 2
from itertools import permutations
testlist = sorted('123456789')
aset = set()
for a,b,c,d,e in permutations(range(1,10), 5):
    i = str(a)
    j = str(b)+str(c)+str(d)+str(e)
    product = str(int(i)*int(j))
    if sorted(product+ i + j) == testlist:
        aset.add(int(product))
    i = str(a)+str(b)
    j = str(c)+str(d)+str(e)
    product = str(int(i)*int(j))
    if sorted(str(int(i)*int(j))+ i + j) == testlist:
        aset.add(int(product))
print(sum(aset))     