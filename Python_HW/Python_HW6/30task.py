# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import os
os.system('clear')


def arithmetic_progression():
    start_num = int(input('Введите первый элемент арифметической прогрессии: '))
    step = int(input('Введите шаг арифметической прогрессии: '))
    amount_num = int(input('Введите количество элементов в арифметической прогрессии: '))
    arithm_prog_list = [start_num + step * i for i in range(amount_num)]
    return arithm_prog_list

list_progression = arithmetic_progression()

print(f'\nАрифметическая прогрессия:', *list_progression)