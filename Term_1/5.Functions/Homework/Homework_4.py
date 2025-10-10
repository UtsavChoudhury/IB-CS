import random
def share(a, b):
    set_a = set(a)
    set_b = set(b) # LISTS WORK TOO; SETS ARE FASTER BUT EXTRA FOR THE COURSE AT THE MOMENT

    for x in set_a:
        if x in set_b:
            return True
    
    return False

a = [random.randint(0, 1000) for i in range(10)]
b = [random.randint(0, 1000) for i in range(10)]

print(a)
print(b)

print(share(a,b))

# I think the any() function also works or something.