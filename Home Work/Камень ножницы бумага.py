
import random

start = input('Вы запустили игру "🪨 Камень, ✂️ ножницы, 📄 бумага". Хотите поиграть? (Введите: 1 или 0): ')

if start == '1':

    user_ball = 0
    comp_ball = 0
    while True:
        print('Чтобы узнать счёт введите: с.')
        print('Чтобы закончить игру введите: 0.')
        print('')
        user = input("🪨 Камень, ✂️ ножницы или 📄 бумага? (Вводите: к, н или б): ")

        list_play = ['к', 'н', 'б']
        if user in list_play:
            comp = random.choice(list_play)
            print(comp)

            if comp == 'к' and user == 'н':
                comp_ball += 1
            if comp == 'к' and user == 'б':
                user_ball += 1
            if comp == 'н' and user == 'к':
                user_ball += 1
            if comp == 'н' and user == 'б':
                comp_ball += 1
            if comp == 'б' and user == 'н':
                user_ball += 1
            if comp == 'б' and user == 'к':
                comp_ball += 1
            if comp == 'к' and user == 'к':
                comp_ball += 0
                user_ball += 0
            if comp == 'н' and user == 'н':
                comp_ball += 0
                user_ball += 0
            if comp == 'б' and user == 'б':
                comp_ball += 0
                user_ball += 0

        elif user == 'с':
            print('Ваши очки: ', user_ball, '.', 'Очки компьютера: ', comp_ball, ".")
        elif user == '0':
            print('Ваши очки: ', user_ball, '.', 'Очки компьютера: ', comp_ball, ".")
            print('Завершение игры!')
            break
        else:
            print('Неверно набрана команда.')
            print('')

if start == '0':
    print('Жаль, что даже не попробовали 8{')
else:
    print('Перезапустите программу')
