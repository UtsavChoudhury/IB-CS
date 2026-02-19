def test(A, B):
    set_A = set(A)
    for i in B:
        if i in set_A:
            return True
    return False

A = [1, 2, 3, 4, 5]
B = [1, 2, 3]

print(test(A, B))