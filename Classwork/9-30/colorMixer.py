selection_1 = ''
selection_2 = ''

selections = [selection_1, selection_2]
colors = ['red', 'yellow', 'blue']

for i, color in enumerate(selections):
    print ('Please select one of three choices: Red, Yellow, Blue:')
    selections[i] = input().lower().strip()
    while selections[i] not in colors:
        print ('Invalid color, Please select one of three choices: Red, Yellow, Blue:')
        selections[i] = input().lower().strip()

if 'red' in selections and 'blue' in selections:
    print ('purple')
elif 'red' in selections and 'yellow' in selections:
    print ('orange')
elif 'blue' in selections and 'yellow' in selections:
    print ('green')
else:
    pass

