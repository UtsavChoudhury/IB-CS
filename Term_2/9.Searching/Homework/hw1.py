def bin_search(key, arr):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        val = arr[mid]

        if val == key:
            print(val)
            return
        elif val > key:
            r = mid - 1
        else: 
            l = mid + 1
        print(val)
    
    return

arr = [-2, 9, 11, 12, 13, 14, 15, 22, 142]
bin_search(15, arr)
