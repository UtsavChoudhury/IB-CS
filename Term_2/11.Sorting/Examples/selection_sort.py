def selection_sort(array):
    for i in range(len(array)): # 0, 1, ..., n-2
        min_value = array[i]
        min_index = i
        for j in range(i+1, len(array)): # i + 1, ..., n-1
            if array[j] < min_value:
                min_value = array[j]
                min_index = j
        if min_index != i:
        # swap values
            array[min_index] = array[i]
            array[i] = min_value
    return array


print(selection_sort([7, 9, 2, 11]))
        
