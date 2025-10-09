from bin_search import bin_search
from seq_search import seq_search
import random
import time
import matplotlib.pyplot as plt

def time_search(algo, n, sort_data=False):
    # Generate n samples with replacement from [0, 1, ..., n-1]
    data = random.choices(range(n), k=n)
    if sort_data:
        data.sort()
    key = n  # Never found, ensures worst case

    start = time.process_time()
    algo(key, data)
    end = time.process_time()
    return end - start

# Input sizes to test
input_sizes = [10**i for i in range(1, 6)]  # 10, 100, 1000, 10000, 100000

# Store results for both algorithms
bin_search_times = []
seq_search_times = []

# Measure time for each input size
for n in input_sizes:
    bin_time = time_search(bin_search, n, sort_data=True)  # Binary search requires sorted data
    seq_time = time_search(seq_search, n, sort_data=False)  # Sequential search doesn't require sorted data

    bin_search_times.append(bin_time)
    seq_search_times.append(seq_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, bin_search_times, label="Binary Search", marker='o')
plt.plot(input_sizes, seq_search_times, label="Sequential Search", marker='o')
plt.xscale('log')  # Logarithmic scale for input sizes
plt.yscale('log')  # Logarithmic scale for time
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Binary Search vs Sequential Search Time Complexity")
plt.legend()
plt.grid(True)
plt.show()