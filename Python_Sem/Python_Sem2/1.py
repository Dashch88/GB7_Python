# 1) По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

import os
os.system('clear')

n = int(input('Введите целое неотрицательное число: '))

factorial_n = 1
while n > 1:
    factorial_n *= n
    n -= 1
print(f'n! = {factorial_n}')