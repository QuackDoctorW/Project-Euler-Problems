count = 0
text = ['a list provided']
        
def istri(num):
    sqrt = (num*2)**(0.5)
    if (sqrt//1)*(sqrt//1+1) == num*2:
        return True
for word in text:
    total = 0
    for letter in word.lower():
        nletter = ord(letter)-96
        total+= nletter
    if istri(total):
        count+=1
print(count)