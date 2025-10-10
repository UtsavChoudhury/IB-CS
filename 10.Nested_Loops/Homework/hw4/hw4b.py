for i in reversed(range(7)): # 6, 5, 4, 3, 2, 1
    for j in range(i):
        if j % 2 == 0:
            print('*', end='')
        else:
            print('-', end='')
    print()