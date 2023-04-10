# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.


# aabacb
# a_1
# a_2
# b_1
# a_3
# c_1
# b_2

import os
os.system('clear')

dict_new = {}
string_new = input('Введите строку: ')

for char in string_new:
    if char in dict_new:
        dict_new[char] += 1
    else:
        dict_new[char] = 1
    print(f'{char}_{dict_new[char]}')