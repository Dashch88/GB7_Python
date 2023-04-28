# Функции для работы с интерфейсом программы

import os
import main
import file_proc

# Меню с командами
def help_menu():
    print(f'\nДоступные команды:\n'
          f'wr -- ввод новых данных в справочник;\n'
          f'r -- вывод всего справочника;\n'
          f'sr -- поиск записи;\n'
          f'chg -- изменение записи;\n'
          f'del -- удаление записи;\n'
          f'help -- для вывода данной подсказки;\n'
          f'q -- для выхода из программы')

# Функция для выбора команды
def start_menu():
    command = None
    while command != "q":
        command = input('\nВы в главном меню. Введите необходимую команду и нажмите enter: \n')
        match command:
            case "help":
                help_menu()
            case "wr":
                main.add_contact()
            case "r":
                main.print_phonebook()
            case "sr":
                main.search_contact()
            case "chg":
                main.change_contact()
            case "del":
                main.del_contact()
            case "q":
                quit()
            case _:
                print('\nВведена неправильная команда!\n')
                

os.system("clear")
print('Здравствуйте. Это программа Телефонный справочник.')
help_menu()
start_menu()
