

n = int(input("Enter a positive integer: "))
if (n < 1):
    print('ERROR: invalid input.')
    exit()

a = n
res = 1
while (n >= 1):
    res *= n
    n -= 1

print(f'{a}! is {res}.')