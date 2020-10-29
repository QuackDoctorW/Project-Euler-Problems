#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#As 1 = 14 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.



#999,999 -> 354,294 (9^5*6) means the largest number a six digit sum of fifth power can represent is 354294, 
#999,9999 -> 413343, cannot represent 7th digits with fifth power; adding 6 9^5 gives you a 6 digit

maxnum = 354294
power = 5
total= 0
for i in range(10,maxnum+1):
    text = str(i) 
    fifthpowersum =0
    for j in text:
        fifthpowersum += int(j)**power
    if fifthpowersum == i:
        total += i
print(total)

#short edition
print(sum(x for x in range(1,354295) if x == sum(int(y)**5 for y in str(x))))
