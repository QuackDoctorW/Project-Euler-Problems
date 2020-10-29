#problem 2, By considering the terms in the Fibonacci sequence whose values 
#do not exceed four million, find the sum of the even-valued terms.

a = 1
b = 2
sum = 2

while a + b <= 4000000:
    a, b = b, a+b
    if b%2 == 0:
        sum += b
print(sum)
4613732