def closest_to_middle(lst, key):
    if len(lst) % 2 == 0:
        return -1  # Only works for odd-length lists
    mid = len(lst) // 2
    min_dist = float('inf')
    result = -1
    for i, val in enumerate(lst):
        dist = abs(val - key)
        if dist < min_dist or (dist == min_dist and i < result):
            min_dist = dist
            result = i
    return lst[result] if result != -1 else -1

# Example usage:
# lst = [1, 5, 9, 12, 20]
# key = 10
# print(closest_to_middle(lst, key))  # Output: 9