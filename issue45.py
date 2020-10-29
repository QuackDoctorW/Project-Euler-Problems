def ispent(num):
    limit = int((num*2/3)**0.5)+1
    for n in range(1,limit+1):
        if n*(3*n-1)/2 == num:
            return True
    return False

def ishex(num):
    limit = int((num/2)**0.5)+1
    for n in range(1,limit+1):
        if n*(2*n-1) == num:
            return True
    return False

n = 286
while True:
    if ispent(n*(n+1)/2) and ishex(n*(n+1)/2):
        print(n,n*(n+1)/2)
        break
    else:
        n+=1
        print(n)