def transpose(a):
    res = []
    for j in range(len(a[0])):
        temp = []
        for i in a:
            temp.append(i[j])
        
        res.append(temp)
    return res




lst = [[1, 2, 3], [4, 5, 6]]

print(transpose(lst))

