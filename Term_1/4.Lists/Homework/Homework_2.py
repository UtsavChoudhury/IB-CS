lst_1 = []
lst_2 = []
while (inp := int(input('Enter an integer: '))) != 0:
    if (inp > 0):
        lst_1.append(inp)
    else:
        lst_2.append(inp)

for x in lst_1:
    print(x, end= ' ')

print("\n")

for x in lst_2:
    print(x, end=' ')