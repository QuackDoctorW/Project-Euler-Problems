maximum = 0 
for a in range(1,101):
    product = 1
    for b in range(1,101):
        product *=a
        maximum = max(maximum, sum(int(i) for i in str(product)))
print(maximum)
    
    