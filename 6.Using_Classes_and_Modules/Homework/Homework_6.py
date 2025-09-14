def max_char_rep(s):
    counter = best = 1
    if s == '':
        return 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            counter += 1

            if counter > best:
                best = counter

        else:
            counter = 1
    
    return best



inp = ['abcd', 'abbbcdd', 'abbbcddddd', '']

for x in inp:
    print(max_char_rep(x))