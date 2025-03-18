names = []
while True:
    new = input("Кого добавим? ")
    if new == 'Список':
        print(names)
    else:
        names.append(new)
        print(f'{new} добавлен')