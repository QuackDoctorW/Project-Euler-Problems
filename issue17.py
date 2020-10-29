digit = {0: 0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10: 3, 11: 6, 12: 6, 13:8,
         14:8, 15:7, 16:7, 17:9, 18:8, 19:9}
tens = {0:0, 2:6, 3:6,4:5,5:5,6:5,7:7,8:6,
         9:6}

def count(num): 
    total = 0
    if num > 100:
        total += 7 + digit[num//100]
        if num %100 != 0 :
            total +=3   
    if num%100 <20:
        return total+ digit[num%100]
    return  total + tens[num%100//10] + digit[num%10]

x = 11 #include 1000

for n in range(1,1000):
    x+=count(n)
print(x)

  
    
    
