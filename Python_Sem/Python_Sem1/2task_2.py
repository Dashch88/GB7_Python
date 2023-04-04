# 2) Напишите программу, которая на вход принимает 5 чисел и находит максимально из них.
# Решение 2:

import os
os.system('clear')

num = int(input('Введите 1-е число: '))
max = num
for i in range(2, 6):
    num = int(input(f'Введите {i}-е число: '))
    if num > max:
        max = num
print(f"Максимально введённое число: {max}")