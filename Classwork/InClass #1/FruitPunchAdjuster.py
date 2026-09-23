cupsOrangeJuice = 3
cupsPineappleJuice = 2
cupsCranberryJuice = 1.5
servings = 12

desiredServings = int(input('Please enter how many servings you want: '))

cupsOrangeJuice = cupsOrangeJuice * desiredServings/servings
cupsPineappleJuice = cupsPineappleJuice * desiredServings/servings
cupsCranberryJuice = cupsCranberryJuice * desiredServings/servings

print (f'{cupsOrangeJuice:.1f} cups orange juice')
print (f'{cupsPineappleJuice:.1f} cups pineapple juice')
print (f'{cupsCranberryJuice:.1f} cups cranberry juice')
