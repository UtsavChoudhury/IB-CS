# 1 The purpose of the program is to test if two lists A and B share an element.

# 2 The program is not efficient because if a match is found, it will continue to iterate over both lists. Thus, it will have a constant
# complexity of O(n*m).

def test(A, B):
    for n in range (len(A)):
        for m in range(len(B)):
            if A[n] == B[m]:
                return True
            
    return False

A = [1, 2, 3, 4, 5]
B = [1, 2, 3]

print(test(A, B))