import random
n = 12
lst = random.sample(list(range(n)), n)

diff_1 = [lst[x] - lst[x-1] for x in range(1, n)]

print(lst)
print(diff_1)

diff_2 = [(next - prev) for prev, next in (zip(lst, lst[1:]))]
# zip() will stop working for the last one because there is no other pair

print(diff_2)