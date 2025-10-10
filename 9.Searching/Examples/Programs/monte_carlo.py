from bin_search import bin_search
from seq_search import seq_search
import random
import time
import matplotlib.pyplot as plt

def time_search(algo, n, sort_data=False, repeats=10): # Jarmo code
    # Generate n samples with replacement from [0, 1, ..., n-1]
    data = random.choices(range(n), k=n)
    if sort_data:
        data.sort()
    key = n  # Never found, ensures worst case

    total_time = 0 # idk if this is useful
    for _ in range(repeats):  # Repeat the search to get an average time
        start = time.perf_counter()  # Higher resolution timer
        algo(key, data)
        end = time.perf_counter()
        total_time += (end - start)
    
    return total_time / repeats  # Return the average time

# Input sizes to test
input_sizes = [i for i in range(100, 50001, 100)] 

# Store results for both algorithms
bin_search_times = []
seq_search_times = []

# Measure time for each input size
for n in input_sizes:
    bin_time = time_search(bin_search, n, sort_data=True, repeats=20)  # Binary search requires sorted data
    seq_time = time_search(seq_search, n, sort_data=False, repeats=20)  # Sequential search doesn't require sorted data

    bin_search_times.append(bin_time)
    seq_search_times.append(seq_time)

# Plot Binary Search Performance
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, bin_search_times, label="Binary Search", marker='o', markersize=4, linewidth=1)
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Binary Search Time Complexity")
plt.grid(True)
plt.legend()
plt.show()

# Plot Sequential Search Performance
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, seq_search_times, label="Sequential Search", marker='o', markersize=4, linewidth=1, color='orange')
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sequential Search Time Complexity")
plt.grid(True)
plt.legend()
plt.show()