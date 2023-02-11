start_num = int(input('Enter the starting number of organisms: '))
daily_increase = float(input('Enter the average daily population increase as a ' + 'percentage: '))
num_days = int(input('Enter the number of days the population will be left to multiply: '))

print('Day   Population')
for day in range(1, num_days + 1):
    if day == 1:
        population = start_num
    else:
        population *= (1 + daily_increase / 100)
    print(format(day), format(population,'12,.2f'))
