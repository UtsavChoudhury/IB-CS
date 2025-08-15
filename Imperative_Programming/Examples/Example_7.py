s = 504053
n = 1
sol_found = False

while (not sol_found):
    if ((n * (n+1)) / 2 > s):
        print(n)
        sol_found = True
    else:
        n += 1