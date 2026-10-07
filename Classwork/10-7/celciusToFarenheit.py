print (f'Celcius:\t Farenheit:')
for tempC in range(0, 21): #third param for step (0, 20, 1) step is one by default
    tempF = 9/5 * tempC + 32
    print (f'{tempC}\t\t {tempF:.2f}')