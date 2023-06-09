# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import os
os.system('clear')

sum = int(input('Введите чему равна сумма загаданных X и Y: '))
prod = int(input('Введите чему равно произведение загаданных X и Y: '))

# находим дискриминант по формуле D = b**2 - 4*c, где b == sum, а c == prod
D = sum ** 2 - 4 * prod
if (D ** 0.5) *10 % 10 == 0:    # проверка дискриминанта на извлечение из корня в натуральное число
    X = int((sum + D ** 0.5) / 2)
    Y = int((sum - D ** 0.5) / 2)
    print(f'Загаданное число X={X}, Y={Y}')
else:
    print('Введены сумма и/или произведение не удовлетворяющие условиям задачи.')