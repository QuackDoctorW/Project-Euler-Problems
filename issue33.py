for denom in range(2,99):
    for num in range(1,denom):
        d = str(denom)
        n = str(num)                 
        for i in d:
            if i in n and int(i) != 0:
                d = d.replace(i,'')
                n = n.replace(i,'')
        if len(d) > 0 and len(n) > 0 and int(d) != 0:
            if int(n) != num:
                if int(n)/int(d) == num/denom: 
                    print(n,d)            
        
