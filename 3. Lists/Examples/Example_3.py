#1
temp = ['there', 'are', 'some', 'words', 'here']
lst_1 = temp

i = 0
while i < len(lst_1):
    if (len(lst_1[i]) <= 4):
        lst_1.pop(i)
    else:
        i += 1
    
print(lst_1)

#2 

lst_2 = [x for x in temp if len(x) > 4]
print(lst_2)

