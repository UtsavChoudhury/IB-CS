def seq_search(arr, key):
    if len(arr) == 0:
        return False
    if arr[0] == key:
        return True
    else:
        return seq_search(arr[1:], key)