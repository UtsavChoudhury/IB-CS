import math
k = 2
n = int(input('Enter a positive integer: '))
upper_bound = int(math.sqrt(n)) + 1

if (n == 1):
    print("Not prime!")
    exit()

if (n == 2):
    print('Prime')
    exit()

while (k <= upper_bound):
    if (n % k == 0):
        print('Not prime!')
        exit()
    
    k += 1

print('Prime!')