names = []
numbers = []
services = []

while True:
    new1 = input("Введите имя: \n")
    new2 = input("Введите номер: \n")
    new3 = input("Введите данные: \n")
    if new1 == 'Список':
        print(names)
    elif new1 == "Номер":
        print(new1)
    else:
        names.append(new1)
        print(f'{new1} добавлен')
        if new2 == 'Список':
            print(names)
        else:
            numbers.append(new2)
            print(f'{new2} добавлен')
            if new3 == 'Список':
                print(names)
            else:
                services.append(new3)
                print(f'{new3} добавлен')

