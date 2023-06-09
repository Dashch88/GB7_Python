# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

import os
os.system('clear')

numOfCranes = int(input('Введите количество журавликов, которые сделали ребята: '))

if numOfCranes % 6 == 0:
    numOfCranesGuys = numOfCranes // 6
    numOfCranesKate = numOfCranesGuys * 4
    print(f'Петя и Серёжа сделали по {numOfCranesGuys}. Катя - {numOfCranesKate}.')
else:
    print('При заданном количестве журавликов задача не имеет решения.')