# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = int(input("Введите число: "))
fibo_prev = 0
fibo_cur = 1
i = 2
while fibo_cur < a:
    fibo_prev, fibo_cur = fibo_cur, fibo_cur + fibo_prev
    i += 1
if fibo_cur == a:
    print(i)
else:
    print(-1)