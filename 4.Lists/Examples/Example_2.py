
lst = []
while (inp := int(input('Enter a nonnegative integer: '))) > -1:
    index = 0
    while index < len(lst) and lst[index] < inp: # We need to put the first condition first, the more critical condition must be first.
        # HANDLES THE CASES WHERE THE SIZE OF THE LIST IS 0 AND WHERE WE NEED TO PUT AT THE END
        index += 1
    lst.insert(index, inp)
    

print(lst)

lst = []
while (inp := int(input('Enter a nonnegative integer: '))) > -1:
    index = len(lst) - 1
    while index > -1 and lst[index] < inp: # We need to put the first condition first, the more critical condition must be first.
        # HANDLES THE CASES WHERE THE SIZE OF THE LIST IS 0 AND WHERE WE NEED TO PUT AT THE END
        index -= 1
    lst.insert(index + 1, inp)
    

print(lst)