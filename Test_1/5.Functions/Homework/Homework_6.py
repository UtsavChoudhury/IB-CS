def alternate(lst):
    res = []
    l = len(lst)
    left = 0
    right = l - 1

    while left <= right:
        if left == right:
            res.append(lst[left])
        else:
            res.append(lst[left])
            res.append(lst[right])
        left += 1
        right -= 1

    return res


print(alternate([1, 2, 3, 4, 5]))