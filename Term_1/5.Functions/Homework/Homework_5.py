def REMOVE(ORIG, X, OUT):
    OUT.clear()                    
    count = ORIG.count(X)        
    OUT.extend([y for y in ORIG if y != X]) 
    OUT.extend([0] * count)
    return OUT

ORIG = [1, 2, 3, 4, 5, 5, 4, 6, 3, 2, 1]
OUT = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]


# OR

print(REMOVE(ORIG, 4, OUT))

ORIG = [1, 2, 3, 4, 5, 5, 4, 6, 3, 2, 1]
OUT = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

OUT = ORIG

print(REMOVE(ORIG, 4, OUT))