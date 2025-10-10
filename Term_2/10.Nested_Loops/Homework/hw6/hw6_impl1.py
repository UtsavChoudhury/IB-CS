def symm_diff(a, b):
    res = []
    for i in a:
        found = False
        for j in b:
            if i == j:
                found = True
                break
        if not found:
            res.append(i)

    for i in b:
        found = False
        for j in a:
            if i == j:
                found = True
                break
        if not found:
            res.append(i)
    
    return res
        
        
a = [4, 4, 6, 11, -2, 3]
b = [5, 11, 11, -3, 3, 5]
print(symm_diff(a, b))