plist = [2]
pset = set(plist)

for n in range(3,1000000,2):
    for p in plist:
        if p*p > n:
            plist.append(n)
            pset.add(n)
            break
        if n%p == 0:
            break

print(111)
'''
plist2 = reversed(plist)
best = 0
bestprime = 0
for prime in plist2:
    total = 0
    term = 0
    for pi in range(len(plist)): #determine the largest term number to fit into the sum
        total += plist[pi]
        if total > prime:
            total-=plist[pi]
            break
        term+=1
    if term <= best:
        print('done')
        break
    start = 0
    stop = start+term
    while term >=best: 
        if total == prime:
            bestprime = prime
            best = term
            break
        else:
            total = total - plist[start] + plist[stop]
            if total > prime:
                term -=1
                start+=1
                total -= plist[stop]
            else:
                start +=1
                stop +=1
print(best,bestprime)
'''

#determine the largest term number to fit into the sum
total = 0
for i in range(len(plist)): 
    total += plist[i]
    if total > plist[-1]:
        total-=plist[i] #determine first total
        term = i #determine highest term
        break

temptotal = total #temp term is the smallest total possible for a certain term number, always start with 2
while term >2: 
    if term%2 ==0:
        if total in pset:
            print(total,term)
            break              
    else:    
        for start in range(len(plist)-term+1):
            if total > plist[-1]:
                break         
            if total in pset:
                print(total,term)
                term = 0
                break
            total = total - plist[start] + plist[start+term]           
    temptotal -= plist[term-1]
    total = temptotal
    term -= 1





    
    



