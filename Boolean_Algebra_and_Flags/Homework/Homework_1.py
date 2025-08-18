
time = int(input('Enter an integer between 0 and 23'))

if (time < 0 or time > 23):
    print("ERROR")
    exit()

sun = input('Is the sun shining? yes/no: ')

shining = (sun == 'yes') # sun == 'yes' will evaluate to a boolean (yes or no) and shining will be assinged this value.

if (shining) or (10 <= time <= 16):
    print('Please use sunscreen')