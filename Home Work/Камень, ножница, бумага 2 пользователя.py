start = input('Вы запустили игру "🪨 Камень, ✂️ ножницы, 📄 бумага". Хотите поиграть? (Введите: 1 или 0): ')

if start == '1':

    user1_ball = 0
    user2_ball = 0
    while True:
        print('Чтобы узнать счёт введите: с.')
        print('Чтобы закончить игру введите: 0.')
        print('')
        user1 = input("🪨 Камень, ✂️ ножницы или 📄 бумага? (Вводите: к, н или б) Первого пользователя: ")
        if user1 == 'с':
            print('Ваши очки: ', user1_ball, '.', 'Очки соперника: ', user2_ball, ".")
        elif user1 == '0':
            print('Ваши очки: ', user1_ball, '.', 'Очки соперника: ', user2_ball, ".")
            print('Завершение игры!')
            break
        user2 = input("🪨 Камень, ✂️ ножницы или 📄 бумага? (Вводите: к, н или б) Второго пользователя: ")
        if user2 == 'с':
            print('Ваши очки: ', user2_ball, '.', 'Очки соперника: ', user1_ball, ".")
        elif user2 == '0':
            print('Ваши очки: ', user2_ball, '.', 'Очки соперника: ', user1_ball, ".")
            print('Завершение игры!')
            break

        list_play = ['к', 'н', 'б']
        if user1 in list_play:
            #comp = random.choice(list_play)
            #print(comp)

            if user1 == 'к' and user2 == 'н':
                user1_ball += 1
            if user1 == 'к' and user2 == 'б':
                user2_ball += 1
            if user1 == 'н' and user2 == 'к':
                user2_ball += 1
            if user1 == 'н' and user2 == 'б':
                user1_ball += 1
            if user1 == 'б' and user2 == 'н':
                user2_ball += 1
            if user1 == 'б' and user2 == 'к':
                user1_ball += 1
            if user1 == 'к' and user2 == 'к':
                user1_ball += 0
                user2_ball += 0
            if user1 == 'н' and user2 == 'н':
                user1_ball += 0
                user2_ball += 0
            if user1 == 'б' and user2 == 'б':
                user1_ball += 0
                user2_ball += 0

        elif user1 == user2  == 'с':
            print('Очки 1 пользователя: ', user1_ball, '.', 'Очки соперника: ', user2_ball, ".")
        elif user1 == user2 == '0':
            print('Очки 1 пользователя: ', user1_ball, '.', 'Очки соперника: ', user2_ball, ".")
            print('Завершение игры!')
            break
        else:
            print('Неверно набрана команда.')
            print('')

if start == '0':
    print('Жаль, что даже не попробовали 8{')
else:
    print('Перезапустите программу')