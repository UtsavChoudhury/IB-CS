# 1 (Traced on paper)

# 2 Purpose: To generate all possible two digit numbers from a list of digits 
# excluding numbers with reperating digits.

# The main issue is that the condition in the while loop is independent
# of the length of NUMS. Hence even if we change nums, it will only
# generate the possibilities for the first 3 digits.

# ORIGINAL

NUMS = [3, 7, 4]
m = 0
while m < 3:
    n = 0
    while n < 3:
        if not (m == n):
            print(10 * NUMS[m] + NUMS[n])
        n = n + 1
    m = m + 1


# FIXED

NUMS = [3, 7, 4]
l = len(NUMS)
m = 0
while m < l:
    n = 0
    while n < l:
        if not (m == n):
            print(10 * NUMS[m] + NUMS[n])
        n = n + 1
    m = m + 1