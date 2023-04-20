# list = [1, 1, 3, 4, 5, 6, 7, 8, 9, 3]
# count = 0
# for i in range (1,len(list)):
#     if list[i] > list[i-1]:
#         count += 1
# print(count)


# Лекция 4

# list = [1, 2, 3, 5, 8, 15, 23, 38]

import os
os.system('clear')


def list_filing(el_num):
    list1 = [int(input(f'Введите {i + 1} элемент массива: '))
             for i in range(el_num)]
    return list1


list_f = list_filing(8)

for i in list_f:
    if i % 2 == 0:
        print(f'({i}, {i ** 2})', end=' ')