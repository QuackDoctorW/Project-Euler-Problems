num = 12322
rollingstr = '23456'
Done = False
while not Done:
    numset = set(str(num))
    for r in rollingstr:
        if set(str(int(r)*num)) != numset:
            break
        if r == '6':
            print(num)
            Done = True
    num+=1
            
