while (inp := input(('Enter a calcuation: '))) != '':
    [a_str, op, b_str] = inp.split()
    a_str = float(a_str)
    b_str = float(b_str)

    if (op == '+'):
        res = a_str + b_str

    elif (op == '-'):
        res = a_str - b_str

    elif (op == '*'):
        res = a_str * b_str
    
    else:
        print('FAILURE; RETRY.')
        continue


    print(res)