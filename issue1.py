#problem 1, find sum of all multiples of 3 and multiples of 5 under 1000
count3 = (1000-0.2)//3
count5 = (1000-0.2)//5
count15 = (1000-0.2)//15
def sumofseq(value:int, term: int) -> int:
    return (1+term)*term/2*value
answer = sumofseq(3,count3) + sumofseq(5,count5) - sumofseq(15,count15)
print(answer)

