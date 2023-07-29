# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

number = input('Введите строку:')
count_dict = {}
total = []
for i in number:
    # if i in count_dict:
    #     count_dict[i] += 1
    # else:
    #     count_dict = 1
    count_dict[i] = count_dict.get(i,0) + 1

    total.append(f'{i}' + (f'_{count_dict[i] - 1}' if count_dict[i] > 1 else '')) 
print(*total)
    
    