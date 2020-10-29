text = '''8C TS KC 9H 4S 7D 2S 5D 3S AC
5C AD 5D AC 9C 7C 5H 8D TD KS
3H 7H 6S KC JS QH TD JC 2D 8S
TH 8H 5C QS TC 9H 4D JC KS JS
7C 5H KC QH JD AS KH 4C AD 4S
5H KS 9C 7D 9H 8D 3S 5D 5C AH'''
order = 'AKQJT98765432'
vdict = {}

value = 14
for o in order:
    vdict[o] = value
    value -=1
inv_vdict = {val: key for key, val in vdict.items()}

def sortnum(num):
    new = sorted([vdict[n] for n in num])
    string = ''
    for entry in new:
        string += inv_vdict[entry]
    return string        
        

def sortsuit(suit):
    string = ''
    for s in sorted(suit):
        string += s
    return string

def score(num,suit):
    high1 = num[-1]
    high2 = ''
    high3 = ''
    high4 = ''
    cons = 0
    for n in range(len(num-1)):
        if num[n+1] == num[n]:
            if n+2 < 5 and num[n+2] == num[n]:
                if n+3 <5 and num[n+3] == num[n]:
                    high4 = num[n]
                high3 = num[n]
                
            else:
                high2= num[n]
        
    
    maxsuit = 0
    maxsuit2 = 0
    
#text mdoification into plays and cards
text = text.split('\n')
for i in range(len(text)):
    text[i] = text[i].split(' ')
    
#split plays into player's hands and sort
for play in text:
    num = ''
    suit = ''
    for card in play:
        num += card[0]
        suit += card[1]
    num1 = sortnum(num[:5])
    num2 = sortnum(num[5:])
    suit1 = sortsuit(suit[:5])
    suit2 = sortsuit(suit[5:])