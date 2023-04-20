# 2) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 - › 11

import os
os.system('clear')


list_new = list(filter(lambda x: x.isnumeric(), input("Введите число: ")))

sum_of_list_numbers = sum(list(map(int, list_new)))
print(sum_of_list_numbers)