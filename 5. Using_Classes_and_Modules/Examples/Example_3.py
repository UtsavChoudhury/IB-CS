def find_all(s, sub):
    left = 0
    res = []
    while (left <= len(s) - 1):
        val = s.find(sub, left)
        if (val != -1):
            res.append(val)
            left = val + 1
        else:
            break
    return res
    
inp = ['aba', 'ab', 'b']

for x in inp:
    print(find_all('ababab', x))