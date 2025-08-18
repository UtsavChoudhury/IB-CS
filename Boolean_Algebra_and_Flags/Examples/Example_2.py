

year = int(input('Please give a year: '))

leap = False

#1

if year % 4 == 0:
    leap = True

if year % 100 == 0:
    leap = False

if year % 400 == 0:
    leap = True

#2

if ((year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)):
    leap = True

#Simplified:
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    leap = True


print(leap)
