# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 

import os
os.system('clear')

def rec_sum(num1, num2):
    if num2 == 0:
        return num1
    return rec_sum(num1 + 1, num2 - 1)

num_a = int(input('Введите a: '))
num_b = int(input('Введите b: '))

print(f'\n{num_a} + {num_b} = {rec_sum(num_a, num_b)}')