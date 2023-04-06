# 4) Есть n чисел. Найти минимум.

import os
os.system('clear')

numbers = int(input('Введите количество чисел: '))
minimum_num = int(input(f'Введите 1-е число: '))

for i in range(1, numbers):
    temp = int(input(f'Введите {i+1}-е число: '))
    if minimum_num > temp:
        minimum_num = temp
print(f'Наименьшее введённое число: {minimum_num}')