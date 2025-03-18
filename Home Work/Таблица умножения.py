while True:
    a = int(input("Введите число: "))
    for i in range(1, 11):
        b = a * i
        print(f'{a} * {i} = {b}')
        