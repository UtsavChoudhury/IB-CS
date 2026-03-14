def read_floats(n):
    values = []
    for i in range(n):
        val = float(input(f'input value {i+1} out of {n}: '))
        values.append(val)
    return values

lst = read_floats(3)
print(lst)
    