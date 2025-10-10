
lst = []
s = set()

while ((inp := int(input('Enter an integer: '))) > 0):
    lst.append(inp)
    s.add(inp)

for x in lst:
    print(x, end= ' ')

for x in s:
    print(x, end=' ')