names = ('Oleg', 'Ivan')
    a = input("Выберитедействие: \n 1- LjДобавилить\n 2- Увидеть ")
    if a == '1':
        name = input('Введите имя новоого контакта')
        if name in names:
            print('имя занято')
        else:
            names.append(name)
            print(f'{name} добавить в список контактов')
            print(names)

    elif a == 2
        print(names)


