def odd(s):
    return int(s) % 2 == 1

def filter_file(filename_in, filename_out, cond):
    try:
        with open(filename_in, 'r') as f1, open(filename_out, 'w') as f2:
            lst = []
            for line in f1:
                try:
                    if cond(line):
                        f2.write(line + '\n')
                except Exception as e:
                    print(f'ERROR LINE: {line} and ERROR: {e} ')
    except Exception as e:
        print(e)
        return
    return