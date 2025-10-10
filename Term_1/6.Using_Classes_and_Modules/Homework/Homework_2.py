def date_of_birth(ssn):
    day = int(ssn[:2]) # Will handle the cases when we have 05 -> 5
    month = int(ssn[2:4]) # Will handle the cases when we have 05 -> 5
    year = int(ssn[4:6])  # Will handle the cases when we have 05 -> 5
    cen = ssn[6]

    if cen == '+':
        year += 1800
    elif cen == '-':
        year += 1900
    else:
        year += 2000
    
    return year, month, day


print(date_of_birth('140589+abcd'))