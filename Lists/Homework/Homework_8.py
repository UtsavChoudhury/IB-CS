lst_1 = []
lst_2 = []

while (inp := input('Enter a word: ')) != '!':
    lst_1.append(inp)

while (inp := int(input('Enter an index: '))) > -1:
    lst_2.append(inp)

print(lst_1)

print(lst_2)

lst_2.sort(reverse=True)

for x in lst_2:
    del lst_1[x]

print(lst_1)
