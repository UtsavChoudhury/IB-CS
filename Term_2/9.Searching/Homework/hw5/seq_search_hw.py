def seq_search(key, array):
    index = 0
    found = False

    while not found and index < len(array):
        if array[index] == key:
            found = True
        index += 1

    return found

array = [-5, 11, -1, 16, 2]
print(seq_search(-5, array))
print(seq_search(10, array))

# OR

def seq_search(key, array):
    index = 0
    found = False

    while index < len(array):
        if array[index] == key:
            return True
        index += 1

    return found
