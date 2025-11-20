



def selection_sort(arr):
    for i in range(len(arr)):
        smallest = arr[i]
        min_ind = i
        for j in range(i, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                min_ind = j
        
        if smallest != arr[i]:
            (arr[i], arr[min_ind]) = (arr[min_ind], arr[i])

    return(arr)


print(selection_sort([4,3,2,1]))