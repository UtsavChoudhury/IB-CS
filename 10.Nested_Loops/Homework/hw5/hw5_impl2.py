def uniques(numbers):
    s = {}
    for i in numbers:
        if i in s:
            return False
        s[i] = True
    
    return True




print(uniques([1, 2, 3, 4, 5]))
print(uniques([1, 2, 3, 3]))