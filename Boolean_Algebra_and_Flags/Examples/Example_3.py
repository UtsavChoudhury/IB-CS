

#if ((vacation := input('Enter whether James is on vacation (yes/no): ')) == 'yes') or ((day := int(input('Enter a day as a 1-based integer: '))) > 5):
   # result = 'True'
#else:
 #   result = 'False'

#print(result)


#

while not (1 <= (weekday := int(input('Please give a day of the week')) <= 7)):
    print('Please provide a valid date')
while (response := input('Enter yes/no') not in ('yes' or 'no')):
    print('Please provide a proper response')


if (weekday == 6 or weekday == 7) or (response == 'yes'):
    response = 'true'
else:
    response = 'false'

print(response)
    


