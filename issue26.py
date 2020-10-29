maxcycle = (0,0)
for d in range(2,1001):
    list1 = [0]
    rtimes10=10
    while rtimes10 not in list1:
        list1.append(rtimes10)
        rtimes10 = (rtimes10 % d) * 10
    if rtimes10 % d == 0:
        cycle = 0
    else: 
        cycle = len(list1)-list1.index(rtimes10)
    if maxcycle[1] < cycle:
        maxcycle = (d, cycle)
print(maxcycle)
    
    