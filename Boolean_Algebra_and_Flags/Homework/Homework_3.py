sol_found = False
n = 1

s = int(input('Enter a positive integer: '))

if (s <= 0):
    print("ERROR")
    exit()

while (not sol_found):
    calc = n**3-10*n**2
    if (calc > s):
        sol_found = True
    else:
        n += 1

print(n, calc)