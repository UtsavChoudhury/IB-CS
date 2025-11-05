try:
    print(float('hello'))
except Exception as e:
    print(type(e))   # prints the type of the exception
    print(e)         # prints the error message


while True:
    try:
        inp = float(input('Enter float: '))
        print(inp)
        break
    except ValueError:
        print('INVALID')