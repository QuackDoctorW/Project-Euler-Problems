dict1 = {}
for i in range(2,6):
    for j in range(2,6):
        dict1[i**j] = 0
print(len(dict1))