# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# 6
# 1 2 3 2 4 1
# 1 + 1 = 2

import os
os.system('clear')


def array_filing(el_num):
    list1 = [int(input(f'Введите {i + 1} элемент массива: '))
             for i in range(el_num)]
    return list1


def searching_couples(list_for_search):
    count_of_couples = 0
    for i in range(len(list_for_search)):
        for j in range(i + 1, len(list_for_search)):
            if list_for_search[i] == list_for_search[j]:
                count_of_couples += 1
    return count_of_couples


array1 = array_filing(int(input(f'Введите размерность массива: ')))
couples_array1 = searching_couples(array1)

print(f'\nМассив: {array1}\nКоличество искомых пар: {couples_array1}')