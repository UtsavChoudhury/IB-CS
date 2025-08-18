a = int(input('Enter a positive integer: '))
b = int(input('Enter a positive integer: '))

n = 1
sol_found = False

while (not sol_found):
    if (n % a == 0) and (n % b == 0):
        sol_found = True
    else:
        n += 1

print(n)