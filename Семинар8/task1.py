def find_contact():
    finder = input('Введите искомый контакт:')
    with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
        for stroka in file:
            if finder.lower() in stroka.lower().split():
                    print(stroka, end = '')

def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    otchestvo = input('Введите отчество: ')
    number = input('Введите номер телефона: ')
    comment = input('Комментарий: ')
    with open('phonebook.txt', 'a', encoding = 'UTF-8') as file:
        file.write(f'\n{surname} {name} {otchestvo} {number} {comment}')

def edit_contact():
    finder = input('Введите искомый контакт:')
    with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
    with open('phonebook.txt', 'r+', encoding = 'UTF-8') as file:
        for stroka in file: 
            if finder.lower() in stroka.lower().split():
                need = stroka
                print(f'Редактировать контакт?{need}')
                answer = input('Введите да/нет: ')
                if answer == 'да':
                    with open('phonebook.txt', 'w+', encoding = 'UTF-8') as file:
                        change = input('Введите изменения:')
                        data.remove(need)
                        data.append(change)
                        for line in data:
                            file.writelines(line)
                else:
                    break

def all_contact():
    with open('C:\\Users\\Ильнур\\Desktop\\Python_Course\\phonebook.txt', 'r', encoding = 'UTF-8') as file:
        file.seek(0)
        for line in file:
            print(line)

def remove_contact():
    finder = input('Введите искомый контакт:')
    with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
    with open('phonebook.txt', 'r+', encoding = 'UTF-8') as file:
        for stroka in file: 
            if finder.lower() in stroka.lower().split():
                need = stroka
                print(f'Удалить контакт?{need}')
                answer = input('Введите да/нет: ')
                if answer == 'да':
                    with open('phonebook.txt', 'w+', encoding = 'UTF-8') as file:
                        for line in data:
                            if line != need:
                                file.writelines(line)
                # if answer == 'нет':
                #     with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
                #         for stroka in file:
                #             print(stroka)
                else:
                    break

def menu_phonebook(menu):
    add_ = 'Добавить контакт'
    remove_ = 'Удалить контакт'
    edit_ = 'Изменить контакт'
    find_ = 'Найти контакт'
    all_ = 'Все контакты'
     
    if menu.lower() == add_.lower():
        add_contact()
    if menu.lower() == find_.lower():
        find_contact()
    if menu.lower() == remove_.lower():
        remove_contact()
    if menu.lower() == edit_.lower():
        edit_contact()
    if menu.lower() == all_.lower():
        all_contact()
    else:
        print('\nВыберите действие из меню:')
    
while True:
    menu = input('\nМеню:\nДобавить контакт\nУдалить контакт\nИзменить контакт\nНайти контакт\nВсе контакты\nВыход\nВыбрать действие:\n')
    exit_ = 'Выход'
    if menu.lower() == exit_.lower():
        break
    menu_phonebook(menu)
       
    
