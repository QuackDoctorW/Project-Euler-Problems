#create days of the month, make month 1 to be march and month 12 to be dec
cdict = {}
for i in range(12):
    cdict[i+1] = 31
for i in [2,4,7,9]:
    cdict[i] = 30
cdict[0] = 28


#Jan 1 1900 and Feb 1 1900 are not sundays, starting at march
days = 28+31+1
count = 0
for i in range(1,1199): # check 12*100-2 =1198 months
    days += cdict[(i)%12]
    if days%7 == 0:
        count += 1
        print(count)
    if i%48 == 0:
        days += 1
   


    
