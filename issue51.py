import math
from itertools import combinations

plist = [2,3]
pset = set(plist)
zero_to_nine_str = ['0','1','2','3','4','5','6','7','8','9']
zero_one_two_str = ['0','1','2']

def isprime(num):
    curr = plist[-1]+2
    while num > plist[-1]:
        for p in plist:
            if p*p > curr:
                plist.append(curr)
                pset.add(curr)
                curr+=2
                break
            elif curr%p == 0:
                curr+=2
                break    
    return num in pset

def gen_index_tuples(raw_index_list):
    index_tuple_list = []
    for p in combinations(raw_index_list,len(raw_index_list)-raw_index_list.count('0')):
        print()
        index_tuple_list.append(tuple(sorted(p)))
    return list(dict.fromkeys(index_tuple_list))   
   
def gen_num_group_list(strnum,index_tuple_list):
    num_group_list = []
    for index_tuple in index_tuple_list:
        num_group_list.append(gen_num_group(strnum,index_tuple))
    return num_group_list

def gen_num_group(strnum,index_tuple):
    num_group = []
    for strdigit in zero_to_nine_str:
        for index in index_tuple:
            if index != 0:
                strnum = strnum[:index]+ strdigit + strnum[index+1:]
        num_group.append(strnum)
    return num_group
        
def primecount8(num_group):
    for str_num in num_group:
        print(str_num)
        count = 0
        if isprime(int(str_num)) and str_num[0] != 0:
            count+=1
    return count>=7 

number = 56003
while number == 56003:
    if isprime(number):
        strnum = str(number)
        digit_dict = {} #create a dictionary to record indexes of 0,1,2; if there is any 
        for digit_index in range(len(strnum)): 
            if strnum[digit_index] in zero_one_two_str: 
                if strnum[digit_index] not in digit_dict: # if the digit is a 0,1,2, we add it to dictionary as a entry of a list
                    digit_dict[strnum[digit_index]] = [digit_index]
                else:
                    digit_dict[strnum[digit_index]].extend([digit_index,0]) #making sure there is always one zero less than swappable indexes
        if digit_dict != {}: #if there is occurence of 0,1,2
            print(digit_dict)
            for strdigit in digit_dict:
                digit_dict[strdigit] = gen_index_tuples(digit_dict[strdigit]) #swapping a list of raw indexes, to a list of index tuples
                print(digit_dict)
                digit_dict[strdigit] = gen_num_group_list(strnum, digit_dict[strdigit]) #swapping a list of index tuples each to a number group
                for num_group in digit_dict[strdigit]:
                    if primecount8(num_group):
                        print(111111111111,numgroup[1])
                        break
    number+=2
                    
                
            
                
                

                
                
            
                
            
                

                

