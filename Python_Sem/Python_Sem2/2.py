# 2) Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# n1 = 0
# n2 = 1
# n3 = 1
# n4 = 2
# n5 = 3

import os
os.system('clear')

A = int(input('Введите натуральное число A, которое больше 1: '))
i = 3
fib_num_0 = fib_num_1  = 1
while fib_num_1 < A:
    fib_num_0, fib_num_1 = fib_num_1, fib_num_0 + fib_num_1
    i += 1
if fib_num_1 == A:
    print(f'Число {A} является {i} числом Фибоначчи.')
else:
    print('-1')