a = input("Выбор: Камень ножницы бумага. Введите к или н или б - ")
b = input("Выбор: Камень ножницы бумага. Введите к или н или б - ")
if a in ['к', 'н', 'б'] and b in ['к', 'н', 'б']:

    if a == "к" and b == "н":
        print('1 Win')
    elif a == "к" and b == "б":
         print('2 Win')
    elif a == "н" and b == "б":
         print('1 Win')
    elif a == "н" and b == "к":
         print('2 Win')
    elif a == "б" and b == "н":
        print('2 Win')
    elif a == "б" and b == "к":
         print('1 Win')
    elif a == b:
        print('No Win')
else:
    print('неверные данные')