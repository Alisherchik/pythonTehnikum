names = ['Loki', 'Thor', 'Hulk', 'Spiderman', '1']
# Заменить 0 элемент
names[0] = 'Oleg'
print(names)
print('')
# Сортировка списка
names.sort()
print(names)
print('')
# Перевернул список
names.reverse()
print(names)
print('')

# Замещение значения
names[names.index('Spiderman')] = 'Tanya'
print(names)
index = names.index('Hulk')
names[index] = 'Vanya'
print(names)