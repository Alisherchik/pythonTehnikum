while True:.


    num1 = int(input("ввод числа - "))
    start = input('Ввод "+" "-" "*" "/" ')
    num2 = int(input('Ввод другого числа - '))

    if start == "+":
        print(num1 + num2)
    elif start == "-":
        print(num1 - num2)
    elif start == "*":
        print(num1 * num2)
    elif start == "/":
        if num2 == 0:
            print('Деление на 0 - нельзя')
        else:
            print(num1 / num2)
    else:
        print('нет такого действия')
