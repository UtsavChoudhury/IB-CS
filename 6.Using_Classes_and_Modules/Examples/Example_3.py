def find_all(s, sub):
    left = 0
    res = []
    while left < len(s) and (i := s.find(sub, left)) >= 0:
        res.append(i)
        left = i + 1
    return res

inp = ['aba', 'ab', 'b']

for x in inp:
    print(find_all('ababab', x))