given = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
given2 = '''3
7 4
2 4 6
8 5 9 3'''

given = given.split("\n")
for row in range(len(given)):
    given[row] = given[row].split()


total = 75

del given[0] #del first row, it's included in total

for counter in range(len(given)): #have to make decision equal to number of rows
    leftcol = 0
    rightcol = 0    

    for row in given:
        leftcol += int(row[0]) #take first item in each col
        rightcol += int(row[-1]) #take last item of each col
    if leftcol > rightcol:
        total += int(given[0][0]) #if leftside larger, take left side for the next num
        print(int(given[0][0]))
        for row in given: 
            del row[-1] #delete the right most number

    else:
        total += int(given[0][-1]) #else take the right
        print(int(given[0][-1]))
        for row in given:
            del row[0] #delete the left most number
    del given[0] #delete the top row, as included in total - now empty

print(total)
    
    
    

