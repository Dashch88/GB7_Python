# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)

import os
os.system('clear')

numbers = [2, 32, 102, 30, 1, 0, 100, 220, 0]

max_num = numbers[0]
i = 1

while i < len(numbers) and numbers[i] != 0:
    if numbers[i] > max_num:
        max_num = numbers[i]
    i += 1
    
print(f'Максимальный элемент {numbers} до первого 0 это {max_num}')