t = 2
val_1 = 1 * (-19) * (-99) + 120000 
best = val_1 - 120000
best_t = 1

while (t <= 100):
    val_2 = t * (t-20) * (t-100) + 120000 
    val_1 = (t-1) * (t-21) * (t-101) + 120000
    delta = val_2 - val_1
    if (delta < best):
        best = delta
        best_t = t
    t += 1

print(best_t)

