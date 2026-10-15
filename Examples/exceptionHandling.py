while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please try again...")

print (f'The number is {x}')