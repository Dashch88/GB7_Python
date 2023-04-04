# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

import os
os.system('clear')

num_slices_vertical = int(input('Введите количество долек по вертикали: '))
num_slices_horizontal = int(input('Введите количество долек по горизонтали: '))
num_slices_break_off = int(input('Введите количество долек, которые надо отломить: '))

if num_slices_break_off > num_slices_vertical * num_slices_horizontal:
    print('Нельзя отломить больше долек, чем есть в шоколадке.')
else:
    if num_slices_break_off % num_slices_vertical == 0 or num_slices_break_off % num_slices_horizontal == 0:
        print('Можно отломить заданное количество долек.')
    else:
        print('Нельзя отломить заданное количество долек.')