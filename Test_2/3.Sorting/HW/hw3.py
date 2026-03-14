def insertion_sort(arr):
    N = len(arr)
    i = 1
    while i < N: 
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val: # Worst case this executes 1, 2, 3, ..., n-1 times -> n(n-1) / 2 -> O(n^2) 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
        i += 1
    return arr  


print(insertion_sort([0, 7, 2, 11]))

# WORST CASE OCCURS WHEN REVERSED ARRAY