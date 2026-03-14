def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return 2 * f(n-1) + f(n-2) - 1


print(f(11))


def iter(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    else:
        k = 1
        curr = 2
        prev = 1

        while k < n:
            (curr, prev) = (2 * curr + prev - 1, curr)
            k += 1
        return curr
    

print(iter(11))
