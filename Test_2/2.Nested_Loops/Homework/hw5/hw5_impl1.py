def uniques(numbers):
    seen = []
    for i in numbers:
        if i in seen:
            return False
        seen.append(i)
    
    return True

print(uniques([1, 2, 3, 4, 5]))
print(uniques([1, 2, 3, 3]))