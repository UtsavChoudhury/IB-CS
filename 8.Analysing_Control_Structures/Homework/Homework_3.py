n = 139
l = 3
d = n // l
z = 1
b = False

while (z < l):
    d = d // l
    z = z + 1
    b = not b

if d != 0 and b:
    print(d, b)
else:
    print(z, not b)