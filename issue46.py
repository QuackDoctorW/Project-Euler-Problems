primelist = [2, 3]

def isprime(n):
    for p in primelist:
        if p*p > n:
            primelist.append(n)
            return True
        elif n%p == 0:
            return False
count = 0
num = 5
while count <1:
    if isprime(num):
        num +=2
    else:
        for p in primelist:
            value = ((num-p)/2)**0.5
            if int(value) == value:
                num+=2
                break
            elif p == primelist[-1]:
                print(num)
                count+=1

                
        

    