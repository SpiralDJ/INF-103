CALORIES_PER_MINUTE = 4.2

caloriesBurned = 0
minutes = 10

while minutes <= 30:
    caloriesBurned = minutes * CALORIES_PER_MINUTE
    print(f'In {minutes} minutes you have burned {caloriesBurned} calories.')
    minutes += 5

caloriesBurned = 0
minutes = 10

print('\nTime:\t Calories Burned:')
while minutes <= 30:
    caloriesBurned = minutes * CALORIES_PER_MINUTE
    print(f'{minutes}\t {caloriesBurned}')
    minutes += 5
