booksPurchased = int(input(''))

books = [8, 6, 4, 2, 0]
points = [60, 30, 15, 5, 0]

pointsEarned = 0

for i, amountBooks in enumerate(books):
    if booksPurchased >= books[i]:
        pointsEarned = points[i]
        break

print (pointsEarned)