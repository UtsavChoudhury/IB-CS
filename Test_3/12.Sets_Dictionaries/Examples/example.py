counts = {}
while (w := input("next word (enter for end)")) != '':
    if w not in counts:
        counts[w] = 1
    else:
        counts[w] += 1

while (w := input("next word (enter for end)")) != '':
    c = counts.get(w, 0)
    counts[w] = c + 1