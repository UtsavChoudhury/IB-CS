def bin_search(key, array):
    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        val = array[mid]

        if val == key:
            return True
        elif val > key:
            hi = mid - 1
        else: 
            lo = mid + 1
    
    return False

array = [3, 6, 87, 112, 135]
print(bin_search(6, array))
print(bin_search(115, array))
