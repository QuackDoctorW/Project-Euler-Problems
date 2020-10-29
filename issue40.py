length = 0
goal = 1
product = 1
for i in range(1,1000000):
    length += len(str(i))
    if length >= goal:
        output = str(i)[-(length-goal)-1]
        product = product *int(output)          
        goal = goal*10
    if goal == 10000000:
        break
print(product)
    
    
        
            
            
            
        
    
    