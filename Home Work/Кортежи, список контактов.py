contacts = ['Sasha', 'Pavel']
while True:

    print("Введите данные контакта: \n"
          "1 - Добавить \n"
          "2 - изменить \n"
          "3 - удалить \n"
          "4 - вывести список \n")
    a = input("Выбор действия: ")

    if a == "1":
        a1 = input("Напишите имя: ")
        contacts.append(a1)
        print(f"{a1} - добавлен в список")
        print(contacts)
        print('')
    elif a == "2":
        print(contacts)
        a2 = input("Укажите, что изменить: ")
        a21 = contacts.index(a2)
        a3 = input(" На что хотите изменить: ")
        contacts[a21] = a3
        print(f"{a2} - изменён на - {a3}")
        print(contacts)
        print('')
    elif a == "3":
        print(contacts)
        a4 = input("Укажите что удалить: ")
        #a41 = contacts.pop(a4)
        a42 = contacts.index(a4)
        contacts.pop(a42)
        print(f"{a4} удалён")
        print(contacts)
        print('')
    elif a == "4":
        print(contacts)
        print('')

    else:
        print("Неверные даные")
