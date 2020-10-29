#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
import math

#set up to find the next largest prime number or declare the current one is the largest one
def nextprime(listtotest):
        nextprime = listtotest[0]
        del listtotest[::
        return nextprime
    
#reduce a num by dividing maximum number of current prime
def dividebyprime(number,prime):
    while number%prime == 0:
            number = number//prime
    return number
        
#
number = 17
currentprime = 1
listtotest = list(range(number+1))
del listtotest[0:2] #del 0,1

dividebyprime(number,currentprime)
print(currentnumber)

while number != 1:
        currenntprime = nextprime(listtotest)
        number = dividebyprime(number,currentprime)
print(currentprime)