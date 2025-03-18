names = ['Sasha']
#Добавление в список
names.append("Pavel")
print(names)
print('')

names=['Loki', 'Spiderman']
#Замещение списков
names.insert(0, 'Thor')
print(names)
print('')
names.insert(1, "ASD")
print(names)
print('')
#Объединение данных списков
names.extend(['Thor', 0, 23, 'Tanos'])
print(names)
print('')
names2 = (['Thor', 0, 23, 'Tanos'])
names.extend(names2)
print(names)
print("")

a = "ABC"
names.append(a)
print(names)
print('')
#"Объединение массивов"
names.extend(a)
print(names)