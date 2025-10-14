from selection_sort import selection_sort
import random
import time
import matplotlib.pyplot as plt

def time_sort(algo, n):
    data = random.choices(range(n), k=n)

    start = time.process_time()
    algo(data)
    end = time.process_time()
    return end - start

input_sizes = [i for i in range(100, 5001, 100)]  # Reduced range for testing

selection_sort_times = []

for n in input_sizes:
    time_taken = time_sort(selection_sort, n)
    selection_sort_times.append(time_taken)

# Plot Selection Sort Performance
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, selection_sort_times, label="Selection Sort", marker='o', markersize=4, linewidth=1, color='orange')
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Selection Sort Time Complexity")
plt.legend()
plt.grid(True)
plt.show()  # Ensure the plot is displayed