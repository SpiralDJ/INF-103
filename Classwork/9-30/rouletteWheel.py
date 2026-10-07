pocketSelection = int(input('Enter a pocket number from 0 - 36:'))
while pocketSelection < 0 or pocketSelection > 36:
        print ('Invalid input. Please try again...')
        pocketSelection = int(input('Enter a pocket number from 0 - 36:'))

nums = [10, 18, 28, 36]

for i, num in enumerate(nums):
    if pocketSelection == 0:
        print ('Green')
        break

    if pocketSelection <= num and i % 2 == 0:
        if pocketSelection % 2 == 0:
            print ('Black')
        else:
            print ('Red')
        break

    else:
        if pocketSelection % 2 == 0:
            print ('Red')
        else:
            print ('Black')
        break
    

if pocketSelection == 0:
    print ('Green')
elif pocketSelection >= 1 and pocketSelection <= 10:
    if pocketSelection % 2 == 0:
        print ('Black')
    else:
        print ('Red')
elif pocketSelection >= 11 and pocketSelection <= 18:
    if pocketSelection % 2 == 0:
        print ('Red')
    else:
        print ('Black')
elif pocketSelection >= 19 and pocketSelection <= 28:
    if pocketSelection % 2 == 0:
        print ('Black')
    else:
        print ('Red')
elif pocketSelection >= 28 and pocketSelection <= 36:
    if pocketSelection % 2 == 0:
        print ('Red')
    else:
        print ('Black')