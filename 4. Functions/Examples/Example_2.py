def interleave(a, b):
    result = []
    for (one_a, one_b) in zip(a, b):
        result.append(one_a)
        result.append(one_b)
    return result


print(interleave([1, 2, 3, 4], [5, 6, 7, 8]))
