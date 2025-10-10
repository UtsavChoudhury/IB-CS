
n = int(input('Enter your hand total: '))

if (n<17):
    result = 'Hit'
elif(n>21):
    result = 'Bust'
else:
    result = 'Stay'

print(result)