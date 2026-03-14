def check_perfect(n):
    sum = 0
    k = 1

    while (k < n):
        if (sum <= n):
            if (n % k == 0):
                sum += k
            k += 1
        else:
            return 0

    if (sum == n):
        return 1
    
    return 0
    

j = 1
while (j < 10000):
    if check_perfect(j):
        print(j, end= ' ')
    j += 1
