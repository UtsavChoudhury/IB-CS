flights = ['AY664', 'BA047', 'AF110', 'LH554', 'AY101']
airlines = ['AY', 'UA', 'LH']

for i in range(len(airlines)):
    airline = airlines[i]
    print(f'{airline}: ', end='')
    for j in range(len(flights)):
        flight = flights[j]
        if (flight.startswith(airline)):
            print(flight, end=' ')
    print()