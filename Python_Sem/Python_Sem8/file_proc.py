# Функция добавления заиси в файл
def write_contact(record):
    phonebook = open('Python_Sem/Python_Sem9/phonebook.txt', 'a')
    phonebook.writelines(record)
    phonebook.close()
    return

# Функция вывода в список всего файла
def read_phonebook():
    all_rec = []
    phonebook = open('Python_Sem/Python_Sem9/phonebook.txt', 'r')
    all_rec = phonebook.readlines()
    phonebook.close()
    return all_rec


# Перезапись всего файла
def rewrite_phonebook(all_rec):
    phonebook = open('Python_Sem/Python_Sem9/phonebook.txt', 'w')
    for record in all_rec:
        phonebook.writelines(record)
    phonebook.close()
    return
