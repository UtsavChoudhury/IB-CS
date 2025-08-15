

sol_found = False
n = 1

while (not sol_found):
    if ((n**3 - 16) % 47 == 0):
        sol_found = True
        print(n)
    else:
        n += 1
