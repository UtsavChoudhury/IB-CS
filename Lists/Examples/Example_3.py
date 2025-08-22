#1
lst_1 = []
while (inp := input('Enter a string ')) != 'stop':
    if len(inp) > 4:
        lst_1.append(inp)

print(lst_1)

#2 
data = []
while (inp := input('Enter a string ')) != 'stop':
    data.append(inp)

lst_2 = [x for x in data if len(x) > 4]
print(lst_2)

