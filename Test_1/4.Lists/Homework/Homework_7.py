lst = []

while (inp := int(input('Enter an integer: '))) > -1:
    if inp in lst:
        lst.remove(inp)
    
    lst.insert(0, inp)

print(lst, end=' ')
