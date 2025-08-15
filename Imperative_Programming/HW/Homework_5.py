a = input("Enter a number for a: ")
b = input("Enter a number for b: ")

#1

if (a >= 100):
    if (b <= 50):
        result = 1
    else:
        result = 0
else:
    result = 0

print(result)

#2

succes = False

if (a >= 100):
    if (b<=50):
        succes = True

if (b>= 100):
    if (a<= 50):
        succes = True

if (not succes):
    print(0)
else:
    print(1)