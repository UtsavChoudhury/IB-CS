#1

print('Ex. 1')

n = 9
while (n < 66):
    print(n, end=' ')
    n += 4

print("\n")

#2

print('Ex. 2')

for x in range(0, 14):
    print(3 * 2**x, end=' ') 

print("\n")

#3

print('Ex. 3')

for x in range(1, 40):
    if (x % 4 == 0):
        print('-1', end=' ')
    else:
        print(x, end=' ')