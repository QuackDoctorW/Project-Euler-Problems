
primelist =[2,3,5,7]
primeset = set(primelist)
count = 0
number = 11
total = 0
def istrunct(num):
    snum1 = str(num)
    snum2 = str(num)
    for i in range(len(str(num))-1):
        if int(snum1[:-i-1]) not in primeset:
            return False
        if int(snum2[i+1:]) not in primeset:
            
            return False
    return True
    
while count <= 10:
    for p in primelist: 
        if p*p > number:
            primelist.append(number)
            primeset.add(number)            
            if istrunct(number):
                total += number
                count+=1
            break
        if number%p == 0:
            break
    number +=2
print(total)
