def bubble_sort_2(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                (array[i], array[i+1]) = (array[i+1], array[i])
                sorted = False
    return array


print(bubble_sort_2([-4, 11, 7, -12, 6, 1]))