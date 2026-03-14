while True:
    try:
        filename = input('please provide filename: ')
        with open(filename, 'ta') as f: # ta: text, append
            print(440, file=f) # if it doesn't exist, it will create a file for this
            # This section will only be executed fully if nothing goes wrong.
        break
    except Exception as e:
        print(f'Operation failed. EXCEPTION: {e}')