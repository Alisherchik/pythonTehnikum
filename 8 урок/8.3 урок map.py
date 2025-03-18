# map() - встроенная функция в Pyton, которая принимает 2 аргумента (фунция())

a = lambda x: x**2
b = map(lambda  x: x**2, [1, 2, 3, 4, 5, 6])
print(a(9))
print(b)
print(list(b))
print(tuple(b))