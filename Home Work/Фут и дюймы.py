a = int(input("Введите высоту в футах: "))
b = int(input("Введите высоту в дюймах: "))

c = a * 12 #Один фут равен 12 дюймам
# с - количество в дюймах
d = (c+b) * 2.54 # Один дюм в сантиметрах

print(d)