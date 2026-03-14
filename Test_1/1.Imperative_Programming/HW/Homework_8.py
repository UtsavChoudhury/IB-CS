
#1

a = 3
res = 1
if (a == 0):
    print(1)
else:
    for x in range(a):
        res *= 3

print(res)


#2

a = 3
b = -2
res = 1
if (a == 0 and b == 0):
    print('ERROR')
elif (a == 0):
    print(1)    
else:
    for x in range(a):
        res *= b
print(res)