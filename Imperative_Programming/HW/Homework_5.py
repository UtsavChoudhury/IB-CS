a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))

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

success = False

if (a >= 100):
    if (b<=50):
        success = True

if (b>= 100):
    if (a<= 50):
        success = True

if (not success):
    print(0)
else:
    print(1)