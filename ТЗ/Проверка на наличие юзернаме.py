names = []

while True:
    new = input("Кого добавим? ")
    if new.lower() in [i.lower() for i in names]:
        print(f"Такой {names} имеется попробуйте другой.")

    else:
        names.append(new)
        print(f"{new}- успешно добавлен")
        print(names)
