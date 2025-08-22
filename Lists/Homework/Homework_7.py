lst_1 = []
lst_2 = []

#2.1
while (inp := int(input('Enter an integer: '))) > -1:
    if inp not in lst_1:
        lst_1.insert(0, inp)
    else:
        lst_1.append(inp)

print(lst_1, end=' ')

#2.2
while (inp := int(input('Enter an integer: '))) > -1:
    if inp in lst_2:
        lst_2.insert(0, inp)
    else:
        lst_2.append(inp)

print(lst_2, end=' ')
