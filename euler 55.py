
trueset = set()
falseset = set()
def ispal(num):
    strnum = str(num)
    revstr = strnum[::-1]
    revnum = int(revstr)
    total = revnum + num
    return (str(total) == str(total)[::-1], total)


def lychrel(num, count = 0):
    if num in trueset:
        return True
    if num in falseset:
        return False
    if count > 50:
        return True
    if ispal(num)[0]:
        return False
    count+=1
    worked = (lychrel(ispal(num)[1],count))
    if worked:
        trueset.add(num)
    else:
        falseset.add(num)
    return worked
        

answer = 0    
for i in range(1, 10001):
    if lychrel(i):
        answer +=1
print(answer)


