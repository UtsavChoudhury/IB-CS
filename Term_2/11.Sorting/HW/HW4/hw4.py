import requests
import time
import matplotlib.pyplot as plt

def test_time(algo, data):
    start = time.process_time()
    algo(data)
    end = time.process_time()
    return end - start

def read_words_from_url(url):
    response = requests.get(url, stream=True)
    words = [word for line in response.iter_lines()
             if (word := line.decode('utf-8').strip()).isalpha()]
    return words

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

url = 'https://websites.umich.edu/~jlawler/wordlist'
orig_lst = read_words_from_url(url)

if not orig_lst:
    raise ValueError("???? something is wrong :(")

input_sizes = [i for i in range(100, 100001, 100)]

selection_sort_times = []

for n in input_sizes:
    arr = orig_lst[:n]
    time_taken = test_time(selection_sort, arr)
    selection_sort_times.append(time_taken)

# Plot Selection Sort Performance
plt.figure(figsize=(7, 10))
plt.plot(input_sizes, selection_sort_times, label="Selection Sort", marker='o', markersize=4, linewidth=1, color='orange')
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Selection Sort Time Complexity")
plt.legend()
plt.grid(True)
plt.show()



