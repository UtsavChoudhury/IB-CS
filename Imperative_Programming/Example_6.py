best_big = 0
best_small = 0
for n in range(1, 51):
    res = n * (n - 30) * (n - 50)
    
    if (res > best_big):
        best_big = res

    if (res < best_small):
        best_small = res

print('BIG:', best_big)
print('SMALL: ',  best_small)