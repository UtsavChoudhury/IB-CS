def f(x):
    return 0.5*(x+(2/x))

def iterate(f, x, n):
    res = []
    val = x
    for i in range(n):
        val = f(val)
        res.append(val)

    return res

print(iterate(f, 1, 6)) # PASS THE FUNCTION OBJECT WITHOUT (). The brackets would try to run it and ask for a parameter. We do not want to run it.