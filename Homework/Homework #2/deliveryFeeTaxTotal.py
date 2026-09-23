deliveryFeeRate = 12 / 100
salesTaxRate = 7 / 100

itemsCost = float(input('Please enter the cost of the items ordered: '))

deliveryFee = itemsCost * deliveryFeeRate
salesTax = itemsCost * salesTaxRate
orderCost = itemsCost + deliveryFee + salesTax

print(f'Item cost: ${itemsCost:.2f}')
print(f'Delivery fee: ${deliveryFee:.2f}')
print(f'Sales tax: ${salesTax:.2f}')
print(f'Total: ${orderCost:.2f}')