names = ['Pavel', 'Ivan', 'Jordan', 5]
for i in range(1,20):
    if 'Pavel' in names:
        print('Pavel есть в списке')
        names.pop()
    else:
        print('Не понимаю о ком вы')