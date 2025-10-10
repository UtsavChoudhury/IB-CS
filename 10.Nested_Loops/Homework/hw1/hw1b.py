n = 6
for i in range (1, n):
    for j in range(i, n - 1 + i): # 5 + i
        print(j, end=' ') 
    print()
    