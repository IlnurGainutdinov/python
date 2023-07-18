from random import randint

days = int(input('Введите количество дней: '))
temp, max_length, count = 0,0,0
for _ in range(days):
    temp = temp + randint(-3,3)
    print(temp, end = ' ')
    if temp > 0:
        count += 1
        if count > max_length:
            max_length = count
    else:
        count = 0
print(f'\nМаксимальное количество теплых дней подряд {max_length}')

