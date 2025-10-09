def uniques(numbers):
    check = []
    for i in numbers:
        if i in check:
            return False
        check.append(i)
    
    return True




print(uniques([1, 2, 3, 4, 5]))
print(uniques([1, 2, 3, 3]))