def counting_sort(array):
    # find largest and smallest elements
    lb = array[0]
    ub = lb
    for i in range(1, len(array)): # O(n)
        elem = array[i]
        if elem < lb: lb = elem
        if elem > ub: ub = elem

    # initialize and find counts
    counts = [0 for _ in range(ub - lb + 1)] # O(k)
    for i in range(len(array)): # O(n)
        counts[array[i] - lb] += 1

    # counts to elements in array
    j = 0 # index into array
    for i in range(len(counts)): # O(k)
        while counts[i] > 0: # O(k) (this will execute k times)
            array[j] = i + lb # O(n) (this whole section will execute n times, once for each element that needs sorting)
            counts[i] -= 1
            j += 1 
