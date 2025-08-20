


while not (1 <= (weekday := int(input('Please give a day of the week'))) <= 7):
    print('Please provide a valid date')
while (response := input('Enter yes/no')) not in ('yes', 'no'):
    print('Please provide a proper response')

if (weekday == 6 or weekday == 7) or (response == 'yes'):
    response = 'true'
else:
    response = 'false'

print(response)
