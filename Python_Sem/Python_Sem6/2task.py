# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два
# соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# 7
# 1 2 1 3 4 2 5
# 1 + 1 = 2

import os
os.system('clear')


def array_filing(el_num):
    list1 = []
    for i in range(el_num):
        list1.append(int(input(f'Введите {i + 1} элемент массива: ')))
    return list1


def search_neighbors(list1):
    count = 0
    for i in range(1, len(list1) - 1):
        if list1[i - 1] < list1[i] > list1[i + 1]:
            count += 1
    return count


array1 = array_filing(int(input(f'Введите размерность массива: ')))
count_neighbors = search_neighbors(array1)

print(f'\nМассив: {array1}\nКоличество искомых элементов: {count_neighbors}')