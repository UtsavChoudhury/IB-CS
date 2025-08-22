import random
n = 10
list_of_lists = [random.sample(list(range(n)), n) for _ in range(5)]

flat = []
for i in list_of_lists:
    for j in i:
        flat.append(j)
