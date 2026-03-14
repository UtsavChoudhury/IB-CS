import math
k = 2
n = int(input('Enter a positive integer: '))
upper_bound = int(math.sqrt(n))

result = True

if (n == 1):
    result = False

elif (n == 2):
    result = True

else: 
    while (k <= upper_bound):
        if (n % k == 0):
            result = False
            break
        k += 1

print(result)