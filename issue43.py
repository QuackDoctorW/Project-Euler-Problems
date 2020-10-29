from itertools import permutations
divisor = [2,3,5,7,11,13,17]
total = 0
for p in permutations(range(0,10),10):
    pnum = ''
    for a in p:
        pnum = pnum + str(a)
    count = 1
    for d in divisor:
        if (p[count]*100+p[count+1]*10+p[count+2])%d == 0:   
            count+=1
        else:
            total -= int(pnum)
            break
    total+= int(pnum)
print(total)



    