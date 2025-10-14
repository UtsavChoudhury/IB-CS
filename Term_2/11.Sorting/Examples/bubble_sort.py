def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubble_sort([-4, 11, 7, -12, 6, 1]))