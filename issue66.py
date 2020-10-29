#set up d list
dlist = []
for i in range(1000):
    dlist.append(i+1)

j = 1
while j**2 <= 1000:
    dlist.remove(j**2)
    j+=1

'''
#set up search
best = 0
for d in dlist:
    print(d)
    n = 1
    while n*n*d != int((n*n*d)**0.5)*(int((n*n*d)**0.5)+2):  
        n+=1
    best = max(best,int((n*n*d)**0.5)+1)
   
        
print(best)


#set up search 
x = 2
while len(dlist) != 0:
    for n in range(1,x):
        num = (x-1)*(x+1)/(n*n)
        if num.is_integer():
            if num <= 1000 and num not in dset:
                dlist.remove(num)
                dset.add(num)
                print(len(dlist))   
                
    x+=1
'''
best = 0
for D in dlist:
    n = 1
    count = 0
    while count == 0:
        num1 = (n*n*D)+2
        if (num1**0.5).is_integer():
            print(D, 111,num1-1)
            best = max(num1-1,best)
            break
        num2 = (n*n*D*2)+2
        if ((num2/2)**0.5).is_integer():
            print(D, 222,num2-1)
            best = max(num2-1,best)
            break
        num3 = (n*n*D)-2
        if (num3**0.5).is_integer():
            print(D, 333,num3+1)
            best = max(num3+1,best)
            break
        num4 = (n*n*D*2)-2
        if ((num4/2)**0.5).is_integer():
            print(D, 444,num4+1)  
            best = max(num4+1,best)
            break
        n+=1
print(best)
