mydict = {}
mydict[0] = 1
product = 1
for i in range(1,10):
    product *= i
    mydict[i] = product
print(mydict)

allsum = 0 
for num in range (3,7*362880)
    total = 0
    string = str(num)
    for j in string:
        total += mydict[int(j)]
    if total == num:
        allsum += num
print(allsum)
