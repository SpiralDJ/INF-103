# no ai used but I did use python docs to learn about f strings
# https://docs.python.org/3/tutorial/inputoutput.html

projectedSales = float(input('Please enter the projected amount of total sales for the fundraiser: '))
clubEarnings = projectedSales * 28/100
print(f"The school club earnings from the fundraiser are ${clubEarnings:.2f}.")