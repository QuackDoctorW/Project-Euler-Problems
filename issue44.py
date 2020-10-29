
'''
aset = set()
alist = []
def ispent(num):
    n =1
    while True:
        if 3*n*n-n > num:
            return False
        if 3*n*n-n == num:
            return True
        n+=1
'''
# Actually contains twice pentagonal numbers
pentag_num_list = [2]
pentag_num_set = set()
def ispent(num):
    while num > pentag_num_list[-1]:
        n = len(pentag_num_list)+1
        pent_n = 3*(n*n) - n
        pentag_num_list.append(pent_n)
        pentag_num_set.add(pent_n)
    return num in pentag_num_set

d = 1
count = 0
while d !=0:
    D = d*(3*d-1)/2
    print(D)
    a = 1
    while True:
        if 6*a*a+5*a > 2*D:
            break
        n = (2*D/a+1-3*a)/6
        if n.is_integer():
            if ispent(6*n*n + 6*a*n + 3*a*a -a - 2*n):
                print(222, D, n, n+a,a)
                d = -1
                break
        a+=1
    d+=1
5482660
1291312
