lst = []
s = set()

while (inp := int(input('Enter an integer: '))) > 0:
    lst.append(inp)
    s.add(inp)

for x in lst:
    print(x, end= ' ')

print('\n')

for x in s:
    print(x, end=' ')

#OR

lst_1 = []
lst_2 = []

while (inp := int(input('Enter an integer: '))) > 0:
    if not (inp in lst_1):
        lst_2.append(inp)
    lst_1.append(inp)

for x in lst_1:
    print(x, end= ' ')

print('\n')

for x in lst_2:
    print(x, end=' ')