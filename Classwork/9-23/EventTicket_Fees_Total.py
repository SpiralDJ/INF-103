serviceFeeRate = 12/100
salesTaxRate = 6/100

ticketPrice = float(input('Please enter the ticket price: '))

serviceFee = ticketPrice * serviceFeeRate
salesTax = ticketPrice * salesTaxRate

totalCost = ticketPrice + serviceFee + salesTax

print (f'Ticket Price: ${ticketPrice:.2f}')
print (f'Service Fee: ${serviceFee:.2f}')
print (f'Sales Tax: ${salesTax:.2f}')
print (f'Total Cost: ${totalCost:.2f}')