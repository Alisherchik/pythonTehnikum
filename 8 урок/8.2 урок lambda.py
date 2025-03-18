# lambda функции - это специальный метод создания функций в Pyton в одну строку
# Чаще всего используются там где нужно сделать простую операцию

a = lambda x: x**2
print(a(5))

def a(x):
    return  x/2
print(a(5))

a = lambda x, y=1: x+y
print(a(5,3))

a = lambda x: x**2
print(a(6))

a = lambda x: x*x
print(a(9))