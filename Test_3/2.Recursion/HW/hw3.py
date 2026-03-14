
def T(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return T(n-1) + (n-1) * T(n-2)



def T_it(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        prev_2 = 1 # T(0)
        prev_1 = 1 # T(1)
        for i in range(2, n+1):
            curr = prev_1 + (i - 1) * prev_2
            prev_2, prev_1 = prev_1, curr
    return curr

print(T(3))
print(T_it(10))
