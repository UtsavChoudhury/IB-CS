n = 6
for i in range(1, n+1): # 1 2 3 4 5 6
    for j in range(i):
        print('*', end='') # 1 time, 2 times, ..., 6 times
    print('_' * (n - i)) # 6 - i -> # 5 times, 4 times, ..., 0 times
    print()
    
