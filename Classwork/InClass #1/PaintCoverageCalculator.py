wallWidthFeet = float(input('Enter the width of the wall (in feet): '))
wallHeightFeet = float(input('Enter the height of the wall (in feet): '))
SqFtPerGallon = float(input('Enter the square feet covered by one gallon: '))

wallArea = wallWidthFeet * wallHeightFeet
gallonsNeeded = wallArea / SqFtPerGallon

print (f'Wall area: {wallArea:.1f} square feet.')
print (f'Gallons needed: {gallonsNeeded:.1f} square feet.')