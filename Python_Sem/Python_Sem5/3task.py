# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# При помощи рекурсии

# 5
# (n):
# 1
# 2
# 3
# 4
# 5
# 5 4 3 2 1

import os
os.system('clear')

def rec_input(num):
    if num == 1:
        return input()
    temp = input()
    list_str = rec_input(num - 1) + ' ' + temp
    return list_str

n = int(input('Введите натуральное число N: '))
print(rec_input(n))