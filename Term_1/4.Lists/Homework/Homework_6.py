import random
n = 10
list_of_lists = [random.sample(list(range(n)), n) for _ in range(5)]

flat_1 = []
for i in list_of_lists:
    for j in i:
        flat_1.append(j)

print(flat_1)

flat_2 = [j for i in list_of_lists for j in i]
print(flat_2)
