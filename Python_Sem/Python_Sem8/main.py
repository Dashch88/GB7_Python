# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import file_proc

# Функция ввода нового контакта пользователем
def add_contact():
    contact = [input('Введите Фамилию: ') + ' ', input('Введите Имя: ') + ' ',
               input('Введите Отчество: ') + ' ', input('Введите номер телефона: '), '\n']
    file_proc.write_contact(contact)
    return


# Функция вывода всего справочника в консоль
def print_phonebook():
    all_rec = file_proc.read_phonebook()
    for i in range(len(all_rec)):
        print(f'{i + 1} {all_rec[i]}', end='')
    return


# Поиск контакта в справочнике
def search_contact():
    contact_for_search = input(
        '\nВведите фамилию, имя, отчество или номер телефона для поиска контакта: ').upper()
    all_rec = file_proc.read_phonebook()
    for i in range(len(all_rec)):
        if contact_for_search in all_rec[i].upper():
            print(f'{i + 1} {all_rec[i]}', end='')
    return


# Функция изменения контакта с возможностью выбора изменяемого объекта
def change_contact():
    contact_for_change = int(
        input('\nВведите номер контакта, который хотите изменить: '))
    all_rec = file_proc.read_phonebook()
    for i in range(len(all_rec)):
        if contact_for_change == i + 1:
            print(f'{i + 1} {all_rec[i]}', end='')
            el_of_rec = input(f'\n1 -- Фамилия\n'
                              f'2 -- Имя\n'
                              f'3 -- Отчество\n'
                              f'4 -- Номер телефона\n'
                              f'0 -- Весь контакт\n'
                              f'Введите номер из меню того, что нужно изменить и нажмите enter: \n')
            match el_of_rec:
                case '1':
                    all_rec[i] = all_rec[i].replace(
                        all_rec[i].split()[0], input('\nВведите фамилию: '))
                case '2':
                    all_rec[i] = all_rec[i].replace(
                        all_rec[i].split()[1], input('\nВведите имя: '))
                case '3':
                    all_rec[i] = all_rec[i].replace(
                        all_rec[i].split()[2], input('\nВведите отчество: '))
                case '4':
                    all_rec[i] = all_rec[i].replace(
                        all_rec[i].split()[3], input('\nВведите номер телефона: '))
                case '0':
                    all_rec[i] = [input('Введите Фамилию: ') + ' ', input('Введите Имя: ') + ' ', input(
                        'Введите Отчество: ') + ' ', input('Введите номер телефона: '), '\n']
                case _:
                    print(
                        '\nВведена команда не из списка! Осуществлён возврат в главное меню.\n')
            file_proc.rewrite_phonebook(all_rec)
            return
    return


# Функция удаления контакта с подтверждением от пользователя
def del_contact():
    contact_for_del = input(
        '\nВведите номер контакта, который хотите удалить, фамилию или имя: ')
    all_rec = file_proc.read_phonebook()
    flag_del = False
    for i in range(len(all_rec)):
        if contact_for_del == str(i + 1) or contact_for_del in all_rec[i].split()[0] or contact_for_del in all_rec[i].split()[1]:
            flag_del = True
            del_answer = input(
                f'Вы действительно хотите удалить эту запись?\n{i + 1} {all_rec[i]}\nY/N?\n')
            if del_answer.upper() == 'Y':
                all_rec.pop(i)
                file_proc.rewrite_phonebook(all_rec)
                return
    if flag_del == False:
        print('Запись для удаления не найдена.')
    return
