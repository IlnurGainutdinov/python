# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint

count_wm = int(input('Введите количество арбузов: '))
print(f'Перед вами {count_wm} арбузов')
max_weight = float('-inf')
min_weight = float('inf')


for _ in range(count_wm):
    current_wm = randint(1000, 30000)
    print(current_wm, end = ' ')
    if current_wm < min_weight:
        min_weight = current_wm
    if current_wm > max_weight:
        max_weight = current_wm
print(f'\nСамый тяжелый арбуз {max_weight}гр\nСамый легкий арбуз {min_weight}гр')    