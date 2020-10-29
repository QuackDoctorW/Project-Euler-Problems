a = 1
b = 1
count = 2
while True:
    (a,b) = (b, b+a)
    count+=1
    if len(str(b)) == 1000:
        print(count)
        break
        
