def symm_diff(a, b):
    res = []
    s_a = {}
    s_b = {}
    for i in a:
        s_a[i] = True
    
    for i in b:
        s_b[i] = True
    
    for i in a:
        if i not in s_b:
            res.append(i)

    for i in b:
        if i not in s_a:
            res.append(i)

    return res

a = [4, 4, 6, 11, -2, 3]
b = [5, 11, 11, -3, 3, 5]
print(symm_diff(a, b))