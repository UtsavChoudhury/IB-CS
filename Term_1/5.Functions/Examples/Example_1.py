def abs_value(x):
    if x >= 0:
        return x
    else:
        return -x

def distance(a, b):
    return abs_value(a - b) 


print(abs_value(-50))
print(abs_value(-4))


print(distance(-4, 2))

