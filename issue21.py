def divisors(num):
    sums = 1
    for i in range(2, num+1):
        if i*i >= num:
            if i*i == num:
                sums +=  i
            return sums
        if num%i == 0:
            sums += i+ num//i
    
amidict = {1:0}
totals = 0
for i in range(2,10000):
    if i not in amidict:
        amidict[i] = divisors(i)
    aminum = amidict[i]
    if aminum > 10000 or aminum == i:
        amidict[aminum] = 0
    if aminum not in amidict:
        amidict[aminum] = divisors(aminum)
    if amidict[aminum] == i:
            totals += i

print(totals)

