# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# Ввод: 5
# Ввод: 1 4 1 2 5 8
# Ввод: 6
# -> 5

import os
os.system('clear')

num_el_list = int(input('Введите количество элементов в списке: '))

list_A = list()
for i in range(num_el_list):
    list_A.append(int(input(f'{i}-й элемент массива: ')))

number = int(input('Введите число к котором будет производиться поиск ближайшего: '))
nearest_num = list_A[0]
i = 1

while nearest_num != number and i < len(list_A):
    if abs(nearest_num - number) > abs(list_A[i] - number):
        nearest_num = list_A[i]
    i +=1
        
print(f'\nВходящий список: {list_A} \nЗаданное число: {number} \nСамый близкий элемент к заданному числу: {nearest_num}') 