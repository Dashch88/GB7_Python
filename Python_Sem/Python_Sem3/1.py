# 1) Дан список чисел. Определите, сколько в нем встречается различных чисел.

import os
os.system('clear')

numbers = [2, 32, 12, 32, 0, 123, 0, 22]
unique_numbers = []

for i in range(0, len(numbers)):
    if numbers[i] not in unique_numbers:
        unique_numbers.append(numbers[i])
print(f'Массив изначальный: {numbers} \nМассив только с уникальными числами: {unique_numbers} \
      \nКоличество уникальных чисел: {len(unique_numbers)}')