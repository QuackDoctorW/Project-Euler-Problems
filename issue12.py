'''
primes = [2,3,5,7,11,13,17,19,23,29,31]
curr = [2,3,5,7,11]
currprod = 2310
def product(alist):
    product = 1
    for i in alist:
        product *= i
    return product
#test if triangular number
#return true or false, using n*(n+1)/2 = triangular number

def trinum(num):
    k = (2*num)**0.5
    if k == int(k): #k i ssuppose to be between n and n+1, cannot be an integer
        return False
    elif int(k)*int(k+1) == 2*num:
        return True
    else:
        return False
while True:
    for i in primes:
        while i <= curr[4]:
            number = currprod*i
            if trinum(number):
                print(number)
                break
    curr = nextlist(curr)
    currprod = product(curr)
'''

def countdiv(num):
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            count += 2
    if int(num**0.5) == num**0.5:
        count -= 1
    return count

A = 1
divA = 1
B = 3
while True:
    divB = countdiv(B)
    if divA*divB > 500:
        print(A*B)
        break
    if A < B:
        (A, B) = (B, A+1)
        divA = divB
    else:
        (A, B) = (B, A+2)
        divA = divB



