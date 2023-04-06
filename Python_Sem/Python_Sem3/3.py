# Напишите программу для печати всех уникальных значений в словаре.

# V : 'S001'
# V : 'S002'
# VI : 'S001'
# VI : 'S005'
# VI: 'S005'
# VII:' S005 '
# ' V ':' S009 '
# ' VIII ':' S007 '

import os
os.system('clear')

dict = {'V': 'S001', 'V': 'S002', 'VI': 'S001', 'VI': 'S005',
        'VI': 'S005', 'VII': ' S005 ', ' V ': ' S009 ', ' VIII ': ' S007 '}

unique_set = set(dict.values())
print(f'Исходный словарь: {dict} \n\nСписок уникальных значений словаря: {unique_set}')