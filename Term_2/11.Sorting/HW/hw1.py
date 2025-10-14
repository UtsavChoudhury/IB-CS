def selection_sort(array):
    print(array) 
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
        print(array)

def bubble_sort(array):
    print(array)
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                print(array)

def print_algo(arr, lst_algo, names_algo):
    for algo, name in zip(lst_algo, names_algo):
        print(name)
        algo(arr.copy())
        

arr = [-4, 11, 7, -12, 6, 1]
names_algo = ['SELECTION SORT', 'BUBBLE SORT']
lst_algo = [selection_sort, bubble_sort]

print(print_algo(arr, lst_algo, names_algo))
