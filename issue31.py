
value = [1, 2, 5, 10, 20, 50, 100, 200]
c = [0, 0, 0, 0, 0, 0, 0, 1]
count = 1

while c[0] != 200:
    for i in range(1,len(c)):          
        if c[i] != 0:                  
            count +=1
            c[i] = c[i]-1              
            fill = 200               
            for j in range(i, len(c)):
                fill -= c[j]*value[j]
            c[i-1] = fill//value[i-1]                   
            fill = fill - c[i-1]*value[i-1]                                   
            c[i-2] = fill//value[i-2]            
            break 
print(count)





