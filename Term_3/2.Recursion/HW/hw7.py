def bits(n, depth, lst):
    if depth == n:
        print(lst)
        return 
    else:
        lst.append(0)
        bits(n, depth + 1, lst)
        lst.pop()
        lst.append(1)
        bits(n, depth + 1, lst)
        lst.pop()

bits(1, 0, [])