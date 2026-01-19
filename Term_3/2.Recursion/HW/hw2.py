def f_1(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    else:
        return n * f_1(n-1)
    
print(f_1(7))


def f_2(n): #1, 2, 3
    prod = 1
    for i in range(1, n+1):
        prod *= i
    
    return prod

print(f_2(6))
