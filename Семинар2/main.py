# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = int(input("Введите число: "))
# i = 1
# f = 1
# while i <= n:
#     f = f * i
#     i += 1
# print(f) 

number = int(input("Введите число: "))

factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print(factorial)
    