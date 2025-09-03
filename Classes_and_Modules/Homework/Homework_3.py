def dashify_substring(s, sub):
    if (sub == ''):
        return s
    s = s.replace(sub, '-' + sub + '-', 1) 
    # NEED TO ASSIGN THE REPLACED VALUE TO S BECAUSE STRINGS ARE IMMUTABLE
    return s

s = ['foo']
s += ['foobar'] * 5
sub = ['o', 'oba', 'f', 'bar', 'cat', '']

for a, b in zip(s, sub):
    print(f'INPUT: {a, b}') 
    print(f'OUTPUT: {(dashify_substring(a, b))}')