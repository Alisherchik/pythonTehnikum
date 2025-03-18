names = []
while True:
    new = input("Кого добавим? ")
    if new in names:
        print("Имя занято")
    elif new == "стоп":
        print("завершение програмы")
        break
        continue
    else:
        names.append(new)
        print(names)