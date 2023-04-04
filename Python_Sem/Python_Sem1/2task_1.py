# 2) Напишите программу, которая на вход принимает 5 чисел и находит максимально из них.
# Решение 1:

import os
os.system('clear')

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
num4 = int(input('Введите четвёртое число: '))
num5 = int(input('Введите пятое число: '))

max = num1

if max < num2:
    max = num2
if max < num3:
    max = num3
if max < num4:
    max = num4
if max < num5:
    max = num5

print(f"Максимально введённое число: {max}")