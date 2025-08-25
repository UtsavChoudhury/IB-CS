
lst = []
while (inp := int(input('Enter a nonnegative integer: '))) > -1:
    index = 0
    while index < len(lst) and lst[index] < inp: # HANDLES THE CASES WHERE THE SIZE OF THE LIST IS 0 AND WHERE WE NEED TO PUT AT THE END
        index += 1
    lst.insert(index, inp)
    

print(lst)