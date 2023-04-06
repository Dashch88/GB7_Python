# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность(сдвиг - циклический) на
# K элементов вправо, K – положительное число.

# 1 2 3 4 5 6 7 8 9
# 2

import os
os.system('clear')

numbers = [1, 2, 3, 4, 5 ,6 ,7]
shift = int(input('Введите количество элементов на которые необходимо сдвинуть список: '))
if shift > len(numbers):
    shift %= len(numbers)
numbers_shifted = numbers[-shift:] + numbers[:-shift]
print(f'Исходный список: {numbers} \nСдвинутый список: {numbers_shifted}')