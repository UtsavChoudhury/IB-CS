import random
import math
# 1.
#  The area of R1 is 2 * 2 = 4
#  The area of R2 is pi*r^2 [r = 1] = pi
#  Hence R2/R1 = pi/4

#2

counter = 0
for x in range(10000):
    val_x = random.uniform(-1, 1)
    val_y = random.uniform(-1, 1)
    if (val_x**2+val_y**2 <= 1):
        counter += 1

print(counter/10000)

print("\n")

print(math.pi/4)


