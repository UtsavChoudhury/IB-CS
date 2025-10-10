from seq_search import seq_search
from bin_search import bin_search

def time_search(algo, n, /, sort_data=False):
    import random, time

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)
    if sort_data: data.sort()
    key = n # never found, ensures worst case

    start = time.process_time()
    algo(key, data)
    end = time.process_time()
    return end - start

print(time_search(bin_search, 10**5, True))