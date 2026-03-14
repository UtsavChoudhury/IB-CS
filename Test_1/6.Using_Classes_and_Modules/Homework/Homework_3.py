def dashify_substring(s, sub):
    if (sub == ''):
        return s
    res = s.replace(sub, '-' + sub + '-', 1) 
    # NEED TO ASSIGN THE REPLACED VALUE TO RES BECAUSE STRINGS ARE IMMUTABLE; 
    # JUST CALLING THE FUNCTION ON s, e.g. s.replace(sub, '-' + sub + '-', 1) won't work.
    return res

s = ['foo']
s += ['foobar'] * 5
sub = ['o', 'oba', 'f', 'bar', 'cat', '']

for a, b in zip(s, sub):
    print(f'INPUT: {(a, b)} + \nOUTPUT: {dashify_substring(a, b)}')