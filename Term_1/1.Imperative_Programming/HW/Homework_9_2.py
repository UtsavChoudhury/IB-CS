best_t = 1
val_1 = 120000
val_2 = (1-20)*(1-100)+120000
best_delta = val_2 - val_1

for i in range(100):
    val_1 = i * (i-20) * (i - 100) + 120000
    val_2 = (i+1) * (i-19) * (i - 99) + 120000

    delta = val_2 - val_1

    if delta < best_delta:
        best_delta = delta
        best_t = i + 1

print(best_t)