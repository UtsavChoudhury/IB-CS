import random
n = 12
lst = random.sample(list(range(n)), n)

diff = [lst[x] - lst[x-1] for x in range(1, n)]

print(lst)
print(diff)