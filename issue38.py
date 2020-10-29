'''
test = sorted('123456789')

highest = 0
ha=0
for a in range(9876,0,-1):
    curr = 0
    digit = 9
    for n in range(1,10):
        if digit <0:
            break        
        elif digit == 0:
            if sorted(str(curr)) == test:
                if curr>highest:
                    highest = curr
                    ha = a
            break
        else:   
            curr += a*n*10**(digit-len(str(a*n)))
            digit -= len(str(a*n))          
print(highest,ha)
'''
test = sorted('123456789')

highest = 0
for a in range(9876,0,-1):
    curr = ''
    for n in range(1,10):
        if len(curr) > 9:
            break        
        elif len(curr) == 9:
            if sorted(curr) == test:
                if int(curr)>highest:
                    highest = int(curr)
            break
        else:   
            curr = curr + str(a*n)       
print(highest)
    
    