# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import os
os.system('clear')

N = int(input('Введите число до которого ищем степени 2: '))
deg = 1
while deg <= N:
    print(deg, end = ' ')
    deg *= 2
print()