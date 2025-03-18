names = ['Loki', 'Spiderman']
names.clear()
print(names)
# Добавление элементов
names.append('Олег')
names.append('ivan')
print(names)
print('')

names = ['Loki', 'Thor', 'Hulk']
#Удаление последний элемент
names.pop()
print(names)
# Удаление показанного значения
names.pop(0)
print(names)
# Удаление выделенного значения
names.remove('Thor')
print(names)