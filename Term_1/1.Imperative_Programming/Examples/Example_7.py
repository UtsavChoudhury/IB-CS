s = 504053
n = 1
sol_found = False

while (not sol_found):
    if ((n * (n+1)) / 2 > s):
        sol_found = True
        print(n)
    else:
        n += 1