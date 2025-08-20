import math

def checkprime(n):
    k = 2
    upper_bound = int(math.sqrt(n)) + 1

    if (n == 1):
        return(0)

    if (n == 2):
        return(1)

    while (k <= upper_bound):
        if (n % k == 0):
            return(0)
        
        k += 1
    
    return(1)


counter = 0
n = 1
while (counter < 100):
    if checkprime(n):
            counter += 1
            print(n, end=' ')
    n += 1



k = 1
while (k < 100):
    if checkprime(k):
            counter += 1
            print(k, end=' ')
    k += 1