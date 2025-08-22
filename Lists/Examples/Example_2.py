
lst = []
while (inp := int(input('Enter a nonnegative integer: '))) > -1:
    lst.append(inp)
    lst.sort() # Not that efficient

print(lst)