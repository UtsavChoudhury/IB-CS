#1
k = [7, 3, -1, -5, -8, - 12]
def fun(x):
    flag = True
    i = 2
    print(flag, i, len(x))
    while flag and i < len(x):
        print(flag, i, len(x), x[i] - x[i-1], x[i-1] - x[i-2], end=' ')
        if x[i] - x[i-1] != x[i-1] - x[i-2]:
            flag = False
        else:
            i += 1
        print(flag, end="\n")
    
    return flag

print(fun(k))

#2 print() staements added.

#3 This function tests if a sequence is an arithmetic sequence, meaning between adjacent elements, is there a constant difference between the ith and (i+1)th term?



