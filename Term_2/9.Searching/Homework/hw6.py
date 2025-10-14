def interpolation_search(arr, key):
    lo = 0
    hi = len(arr) - 1

    while (lo <= hi):
        if arr[lo] == arr[hi]:
            if arr[lo] == key:
                return lo
            return -1
            
        i = lo + ((key - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo]) # integer division required

        if i < lo or i > hi:
            return -1
        
        val = arr[i]

        if val == key:
            return i

        if (val > key):
            hi = i - 1
        
        if (val < key):
            lo = i + 1

    return -1

# OR 

def interpolation_search(arr, key):
    lo = 0
    hi = len(arr) - 1

    while (lo <= hi and arr[lo] <= key <= arr[hi]):
        if arr[lo] == arr[hi]:
            if arr[lo] == key:
                return lo
            return -1
            
        i = lo + ((key - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo]) # integer division required

        val = arr[i]

        if val == key:
            return i

        if (val > key):
            hi = i - 1
        
        if (val < key):
            lo = i + 1

    return -1

        


        