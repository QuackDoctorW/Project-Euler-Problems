#Starting in the top left corner of a 2×2 grid, and only being able to move to 
#the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
import math
d = 20
product = 1
for i in range(d):
    product *= (i+21)/(i+1)
print(product//1+1)