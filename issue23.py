abun = []

for num in range(12, 28183-12+1):
    total = 1
    for i in range(2,num):
        if i*i >= num:
            if i*i == num:
                total += i
            break
        if num%i == 0: 
            total += i + num//i
    if total > num:
        abun.append(num)

print(abun)
checkset = set()
for i in abun:
    for j in abun:
        if i+ j > 28123: 
            break
        else:
            if (i+j) not in checkset:
                checkset.add(i+j)   
print((1+28123)*28123/2-sum(checkset))


'''
#too slow
abunset = (abun)
sums = 0
for num in range(24, 28183+1):
    for i in abun:
        if i > num/2:
            break
        if (num - i) in abunset:
            sums += num
            break
print(sums)

'''