a = 46
b = 15
c = 87

ab = a - b
ac = a - c
bc = b - c

if ab * bc > 0:
    result = b
elif ab * ac < 0:
    result = a
else:
    result = c

print(result)