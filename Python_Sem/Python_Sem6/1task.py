# 39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива


import os
os.system('clear')

def array_filing(el_num):
    list1 = []
    for i in range(el_num):
        list1.append(int(input(f'Введите {i + 1} элемент массива: ')))
    return list1

def array_comparison(list1, list2):
    list_fin = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            list_fin.append(list1[i])
    return list_fin


array1 = array_filing(int(input(f'Введите размерность первого массива: ')))
array2 = array_filing(int(input(f'Введите размерность второго массива: ')))

array_fin = array_comparison(array1, array2)

print(f'\nПервый массив: {array1}\nВторой массив: {array2}\n\nЭлементы, которых нет во втором массиве: {array_fin}')