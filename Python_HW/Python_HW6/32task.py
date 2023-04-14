# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import os
os.system('clear')


def list_filing(el_num):
    list1 = [int(input(f'Введите {i + 1} элемент массива: '))
             for i in range(el_num)]
    return list1


def range_elements(list_for_searching):
    print('Введите диапазон поиска (сначала min, потом max):')
    range_search = [int(input()) for i in range(2)]
    list_index = []
    for i in range(len(list_for_searching)):
        if range_search[0] <= list_for_searching[i] <= range_search[1]:
            list_index.append(i)
    return list_index

list_w_el = list_filing(int(input('Введите размерность списка: ')))
list_w_index_in_range = range_elements(list_w_el)

print(f'Элементы подходящие под заданный диапазон имеют индексы: {list_w_index_in_range}')