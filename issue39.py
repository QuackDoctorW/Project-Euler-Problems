
def HeLikesMe(per,s1,s2):
    if (per-s1-s2)**2 == s1*s1+s2*s2:
        return True


expectation=(0,0)
for more in range(3,1000):
    kisses = 0
    for every in range(1,more//3+1):
        for day in range(every,(more-every)//2):
            if HeLikesMe(more,every,day):
                kisses+=1
    if kisses > expectation[1]:
        Pounce
        expectation = (more,kisses)
print(expectation)


