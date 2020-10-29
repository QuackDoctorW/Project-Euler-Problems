#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

sum = 1000
for a in range(1,sum//3):
    for b in range (a+1,(sum-1-a)//2+1):
        if a**2+b**2==(sum-a-b)**2:
            print(a,b,(sum-a-b),a*b*(sum-a-b))
'''
didnt work below
print(a*b*(1000-a-b) for a in range(1,333) for b in range(a+1,(999-a)//2+1) if a**2+b**2==(sum-a-b)**2)
'''