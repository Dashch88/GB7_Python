# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0

import os
os.system('clear')

num = int(input('Введите трёхзначное число: '))
sum = 0

if num // 1000 == 0 and num // 100 != 0:
    for i in range(3):
        sum += num % 10
        num //= 10
    print(f'Сумма цифр введённого числа: {sum}')
else:
    print("Введено не трёхзначное число")