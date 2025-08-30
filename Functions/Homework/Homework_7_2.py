def apply_functions(fs, x):
    func = fs[-1] 
    res = func(x)
    for i in range(len(fs) - 2, -1, -1):
        func = fs[i]
        res = func(res)

    return res

fs = ['...'.join, str.split, str.lower] # We do not give the () when passing a function. If you write str.lower(), it would call the function immediately. Instead, we store the function object.
x = 'WHAT IS THIS?'


print('hello'.upper())
print(str.upper('hello')) # BOTH OF THESE WORK; when we use func(x), x goes in the place of hello here.

print(apply_functions(fs, x))