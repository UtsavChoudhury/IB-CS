def read_ints():
    lst = []
    while (inp := input('Enter an integer: ')) != '':
        lst.append(int(inp))
    return lst

print(read_ints())