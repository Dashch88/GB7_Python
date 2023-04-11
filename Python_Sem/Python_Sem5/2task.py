# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

import os
os.system('clear')

def prime_number(num):
    flag_prime = True
    if num == 1:
        print('Введённое число является простым.')
    else:
        i = 2
        while flag_prime and i < num // 2 + 1:
            if num % i == 0:
                flag_prime = False    
            i += 1
        if flag_prime:
            print('Введённое число является простым.')
        else:
            print('Введённое число НЕ является простым.')    
    return

number = int(input('Введите целое число: '))
prime_number(number)