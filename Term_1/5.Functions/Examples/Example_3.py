def swap(lst, ind1, ind2):
    (lst[ind1], lst[ind2]) = (lst[ind2], lst[ind1])

lst = list(range(1, 14))
print(lst)
swap(lst, 3, 6)
print(lst)