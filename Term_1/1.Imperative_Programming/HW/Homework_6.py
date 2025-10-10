#1
    # a. p(4) = 3 + (4-2)*2 = 3 + 4 = 7
    # b. p(w) = 3 + (w-2)*2 = 3 + 2 * w - 4 = 2 * w - 1 
#2
    # a. P(11) = p(5) + (11-5)*3 = 18 + p(5) = 18 + 3 + 3*2 = 27
    # b. p(w) = (w-5)*3 + P(5) = (w-5)*3 + 3 + (5-2)*2 = (w-5)*3 + 9 = 3 * w - 15 + 9 = 3 * w - 6


w = int(input('Enter a positive integer: '))

if (w <= 2):
    result = 3
elif (2 < w <= 5): # since we already know w > 2 here
    result = 2 * w - 1
else:
    result = 3 * w - 6

print(result)