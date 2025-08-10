

sol_found = False
n = 1

while (not sol_found):
    if ((n**3 - 16) % 47 == 0):
        print(n)
        sol_found = True
    else:
        n += 1
