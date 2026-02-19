observations = [1, 2, 3, 4]
frequencies = [7, 4, 11, 9]
rel_freqs = [0, 0, 0, 0] # Intialised with 0's.

count = 0
i = 0
while i < len(frequencies): # Fixed, < not <=. Out-of-bounds fixed.
    count += frequencies[i]
    i += 1

for (i, f) in enumerate(frequencies):
    val = f / count # Fixed -> will give float
    rel_freqs[i] = val

for (o, r) in zip(observations, rel_freqs): # Now defined
    print(f'{o} : {r}')
