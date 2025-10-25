def bubble_sort_1(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubble_sort_1([-4, 11, 7, -12, 6, 1]))

def bubble_sort_2(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                (array[i], array[i+1]) = (array[i+1], array[i])
                sorted = False
    return array


print(bubble_sort_1([-4, 11, 7, -12, 6, 1]))
