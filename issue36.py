def tobinary(num: int) -> int:
    if num <2:
        return str(num)
    return tobinary(num//2)+str(num%2)
  
palind = []
for i in range(1,1000):
    palind.append(int(str(i)+str(i)[-1::-1]))
    palind.append(int(str(i)+str(i)[-2::-1]))

total = 0
for p in palind:
    binary = str(tobinary(p))
    if binary[:len(binary)//2] == binary[:-1-len(binary)//2:-1]:
        total += p

print(total)
'''
    
    
        
    



        
    
    
